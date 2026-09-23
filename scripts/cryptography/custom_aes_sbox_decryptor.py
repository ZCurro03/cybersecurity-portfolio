"""
Custom AES-128 SBOX Decryptor

This script bypasses standard AES-128-CBC key derivation by exploiting a structurally weak 
(linear) custom SBOX. It decrypts the ciphertext block by block without extracting the original key, 
using a Known-Plaintext Attack (KPA) based on file format signatures (PNG magic bytes).

Required Data & Files:
- 'IV_HEX': The Initialization Vector in hexadecimal format.
- 'CUSTOM_SBOX': The modified linear 256-byte SBOX array extracted from the challenge instructions.
- Encrypted file: The target cipher file in the same directory.

Generated Output:
The script applies a derived cryptographic mask to unravel the cipher, recovers the original 
binary data (PNG image), and saves it to disk, printing the progress and the derived mask to the console.
"""

import binascii

# ==========================================
# 1. PURE PYTHON AES-128 DECRYPTION
# ==========================================

def xtime(a):
    """
    Galois Field (GF) multiplication by 2.
    It shifts the bits left and applies an XOR with the irreducible polynomial 0x1B if an overflow occurs.
    """

    return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def multiply(a, b):
    """
    Galois Field multiplication used in the MixColumns step.
    Iteratively multiplies two 8-bit polynomials in GF(2^8) using the xtime function.
    """

    res = 0
    while b:
        if b & 1: res ^= a
        a = xtime(a)
        b >>= 1
    return res

def inv_mix_columns(state):
    """
    Reverses the diffusion step of AES by multiplying the state matrix by 
    the inverse Maximum Distance Separable (MDS) matrix (14, 11, 13, 9) in the Galois Field.
    """

    for i in range(4):
        c0, c1, c2, c3 = state[i*4 : i*4+4]
        state[i*4]   = multiply(c0, 14) ^ multiply(c1, 11) ^ multiply(c2, 13) ^ multiply(c3, 9)
        state[i*4+1] = multiply(c0, 9)  ^ multiply(c1, 14) ^ multiply(c2, 11) ^ multiply(c3, 13)
        state[i*4+2] = multiply(c0, 13) ^ multiply(c1, 9)  ^ multiply(c2, 14) ^ multiply(c3, 11)
        state[i*4+3] = multiply(c0, 11) ^ multiply(c1, 13) ^ multiply(c2, 9)  ^ multiply(c3, 14)
    return state

def inv_shift_rows(state):
    """
    Reverses the ShiftRows step of AES.
    It cyclically shifts the last three rows of the state matrix to the right
    by 1, 2, and 3 byte positions respectively, undoing the diffusion step.
    """

    # Shift row 1 right by 1
    state[1], state[5], state[9], state[13] = state[13], state[1], state[5], state[9]
    # Shift row 2 right by 2
    state[2], state[6], state[10], state[14] = state[10], state[14], state[2], state[6]
    # Shift row 3 right by 3
    state[3], state[7], state[11], state[15] = state[7], state[11], state[15], state[3]
    return state

def key_expansion(key, sbox):
    """
    Expands the initial 16-byte cipher key into a full 176-byte key schedule
    required for all AES-128 rounds, utilizing the provided SBOX and round constants (rcon).
    """

    rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
    key_schedule = list(key)
    for i in range(16, 176, 4):
        temp = key_schedule[i-4:i]
        if i % 16 == 0:
            temp = [sbox[temp[1]], sbox[temp[2]], sbox[temp[3]], sbox[temp[0]]]
            temp[0] ^= rcon[i//16 - 1]
        key_schedule.extend([key_schedule[i-16+j] ^ temp[j] for j in range(4)])
    return key_schedule

def add_round_key(state, round_key):
    """
    Applies a bitwise XOR operation between the current AES state matrix
    and the round key (subkey) derived for the current round.
    """

    for i in range(16):
        state[i] ^= round_key[i]
    return state

def inv_sub_bytes(state, inv_sbox):
    """
    Reverses the SubBytes step by substituting each byte in the current
    state matrix with its corresponding value from the precomputed inverse SBOX.
    """

    for i in range(16):
        state[i] = inv_sbox[state[i]]
    return state

def decrypt_block(ciphertext, key_schedule, inv_sbox):
    """
    Executes standard AES-128 decryption rounds in reverse order (InvShiftRows, 
    InvSubBytes, AddRoundKey, InvMixColumns) utilizing the custom inverse SBOX.
    """

    state = list(ciphertext)
    state = add_round_key(state, key_schedule[160:176])
    for round_num in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state, inv_sbox)
        state = add_round_key(state, key_schedule[round_num*16 : (round_num+1)*16])
        state = inv_mix_columns(state)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state, inv_sbox)
    state = add_round_key(state, key_schedule[0:16])
    return state

def aes_cbc_decrypt(ciphertext, key, iv, sbox):
    """
    Performs full AES-128 decryption in Cipher Block Chaining (CBC) mode.
    It computes the inverse SBOX, expands the dummy key, decrypts each 16-byte block
    using the core AES inverse functions, and XORs the result with the previous
    ciphertext block (or the IV for the first block) to undo the CBC chaining.
    """

    # Compute the Inverse S-Box for decryption
    inv_sbox = [0] * 256
    for i in range(256):
        inv_sbox[sbox[i]] = i

    key_schedule = key_expansion(key, sbox)
    plaintext = bytearray()
    prev_block = list(iv)

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        # Pad if the last block is incomplete (shouldn't happen in proper AES)
        if len(block) < 16:
            block += bytes([0] * (16 - len(block)))
            
        decrypted_block = decrypt_block(block, key_schedule, inv_sbox)
        
        # CBC Mode: XOR with previous ciphertext block (or IV)
        for j in range(16):
            plaintext.append(decrypted_block[j] ^ prev_block[j])
        prev_block = list(block)

    return bytes(plaintext)


# ==========================================
# 2. THE ATTACK LOGIC
# ==========================================

def solve_ctf(encrypted_filepath, output_filepath, iv_hex, sbox):
    # 1. Read encrypted file and decode IV
    with open(encrypted_filepath, "rb") as f:
        ciphertext = f.read()
    iv = binascii.unhexlify(iv_hex)

    # 2. Perform dummy decryption
    # An arbitrary 16-byte dummy key. Since the custom SBOX is strictly linear, the cipher
    # doesn't properly mix the key and plaintext. Any key works to unravel the block chaining.
    dummy_key = b"A" * 16
    print("[*] Decrypting with dummy key... (this might take a few seconds)")
    dummy_pt = aes_cbc_decrypt(ciphertext, dummy_key, iv, sbox)

    # 3. Derive the mask using known plaintext (PNG Header)
    # The standard 16-byte signature of a PNG file. Used for the Known-Plaintext Attack
    # to deduce the static constant mask generated by the dummy key.
    # Structure: 8 bytes magic number + 4 bytes chunk length + 4 bytes chunk type.
    known_png_header = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52"

    print("[*] Calculating mask from block 0...")
    mask = [dummy_pt[i] ^ known_png_header[i] for i in range(16)]
    print(f"[+] Mask derived: {[hex(m) for m in mask]}")

    # 4. Apply the mask to the entire dummy plaintext
    print("[*] Applying mask to full payload...")
    real_pt = bytearray()
    for i in range(len(dummy_pt)):
        real_pt.append(dummy_pt[i] ^ mask[i % 16])

    # 5. Write the recovered PNG to disk
    with open(output_filepath, "wb") as f:
        f.write(real_pt)
    print(f"[+] Success! Decrypted file saved to {output_filepath}")


# ==========================================
# 3. EXECUTION
# ==========================================

if __name__ == "__main__":
    # Initialization Vector (IV) extracted from the challenge instructions (usually the filename).
    # Replace 'your_iv_hex_here' with the actual IV in hexadecimal format.
    # Example IV: "0123456789abcdef0123456789abcdef"
    IV_HEX = "your_iv_hex_here"

    # The linearly modified 256-byte SBOX extracted from the challenge communication.
    # This deliberately weak substitution box replaces the standard non-linear Rijndael SBOX.
    CUSTOM_SBOX = [
        0x65, 0x64, 0x61, 0x60, 0x75, 0x74, 0x71, 0x70,
        0x25, 0x24, 0x21, 0x20, 0x35, 0x34, 0x31, 0x30,
        0x7e, 0x7f, 0x7a, 0x7b, 0x6e, 0x6f, 0x6a, 0x6b,
        0x3e, 0x3f, 0x3a, 0x3b, 0x2e, 0x2f, 0x2a, 0x2b,
        0x09, 0x08, 0x0d, 0x0c, 0x19, 0x18, 0x1d, 0x1c,
        0x49, 0x48, 0x4d, 0x4c, 0x59, 0x58, 0x5d, 0x5c,
        0x12, 0x13, 0x16, 0x17, 0x02, 0x03, 0x06, 0x07,
        0x52, 0x53, 0x56, 0x57, 0x42, 0x43, 0x46, 0x47,
        0xce, 0xcf, 0xca, 0xcb, 0xde, 0xdf, 0xda, 0xdb,
        0x8e, 0x8f, 0x8a, 0x8b, 0x9e, 0x9f, 0x9a, 0x9b,
        0xd5, 0xd4, 0xd1, 0xd0, 0xc5, 0xc4, 0xc1, 0xc0,
        0x95, 0x94, 0x91, 0x90, 0x85, 0x84, 0x81, 0x80,
        0xa2, 0xa3, 0xa6, 0xa7, 0xb2, 0xb3, 0xb6, 0xb7,
        0xe2, 0xe3, 0xe6, 0xe7, 0xf2, 0xf3, 0xf6, 0xf7,
        0xb9, 0xb8, 0xbd, 0xbc, 0xa9, 0xa8, 0xad, 0xac,
        0xf9, 0xf8, 0xfd, 0xfc, 0xe9, 0xe8, 0xed, 0xec,
        0xff, 0xfe, 0xfb, 0xfa, 0xef, 0xee, 0xeb, 0xea,
        0xbf, 0xbe, 0xbb, 0xba, 0xaf, 0xae, 0xab, 0xaa,
        0xe4, 0xe5, 0xe0, 0xe1, 0xf4, 0xf5, 0xf0, 0xf1,
        0xa4, 0xa5, 0xa0, 0xa1, 0xb4, 0xb5, 0xb0, 0xb1,
        0x93, 0x92, 0x97, 0x96, 0x83, 0x82, 0x87, 0x86,
        0xd3, 0xd2, 0xd7, 0xd6, 0xc3, 0xc2, 0xc7, 0xc6,
        0x88, 0x89, 0x8c, 0x8d, 0x98, 0x99, 0x9c, 0x9d,
        0xc8, 0xc9, 0xcc, 0xcd, 0xd8, 0xd9, 0xdc, 0xdd,
        0x54, 0x55, 0x50, 0x51, 0x44, 0x45, 0x40, 0x41,
        0x14, 0x15, 0x10, 0x11, 0x04, 0x05, 0x00, 0x01,
        0x4f, 0x4e, 0x4b, 0x4a, 0x5f, 0x5e, 0x5b, 0x5a,
        0x0f, 0x0e, 0x0b, 0x0a, 0x1f, 0x1e, 0x1b, 0x1a,
        0x38, 0x39, 0x3c, 0x3d, 0x28, 0x29, 0x2c, 0x2d,
        0x78, 0x79, 0x7c, 0x7d, 0x68, 0x69, 0x6c, 0x6d,
        0x23, 0x22, 0x27, 0x26, 0x33, 0x32, 0x37, 0x36,
        0x63, 0x62, 0x67, 0x66, 0x73, 0x72, 0x77, 0x76
    ]

    # Target ciphertext file. Must be in the same directory or provide full path.
    ENCRYPTED_FILE = "challenge_target_file.enc"
    # Destination file for the decrypted output.
    OUTPUT_FILE = "decrypted_output.png"

    # Verify SBOX is the correct length before running
    if len(CUSTOM_SBOX) != 256:
        print(f"Warning: SBOX length is {len(CUSTOM_SBOX)}. It must be exactly 256.")
    elif IV_HEX == "your_iv_hex_here":
        print("Please replace 'your_iv_hex_here' with a valid Initialization Vector.")
    else:
        solve_ctf(ENCRYPTED_FILE, OUTPUT_FILE, IV_HEX, CUSTOM_SBOX)
