"""
Vigenère Cipher Decoder

This script automates the decryption of texts encrypted with the classical
Vigenère polyalphabetic substitution cipher.

It dynamically maps the provided keyword to the ciphertext, preserving the
original formatting (uppercase, lowercase) and bypassing special characters,
numbers, and non-ASCII characters (like Spanish accents) without altering them
or consuming key letters.

Required Data:
- 'TARGET_CIPHERTEXT': The encrypted string you want to decode.
- 'DECRYPTION_KEY': The keyword used for the cipher.

Generated Output:
The script prints the decrypted plaintext to the console.
"""

# ==========================================
# 1. ALGORITHM IMPLEMENTATION
# ==========================================

def decrypt_vigenere(ciphertext, key):
    """
    Applies a reverse Vigenère cipher shift to a given string using a keyword.
    The shift for each character is determined dynamically by the corresponding
    letter in the repeating key.
    """

    decrypted_chars = []

    # Standardize the key to uppercase to easily calculate shift values (0-25)
    key = key.upper()
    key_index = 0
    key_length = len(key)

    for char in ciphertext:
        # Check if the character is a standard ASCII letter (a-z, A-Z).
        if char.isalpha() and char.isascii():
            # Determine the ASCII base depending on whether the letter is upper or lower case
            ascii_base = ord('A') if char.isupper() else ord('a')

            # 1. Calculate the shift value from the current key letter (A=0, B=1, ..., Z=25).
            shift = ord(key[key_index]) - ord('A')

            # 2. Normalize the character to a 0-25 range.
            # 3. Subtract the shift key to decrypt.
            # 4. Apply modulo 26 to handle alphabet wrap-around.
            # 5. Add the base back to get the final readable ASCII character.
            shifted_char = chr((ord(char) - ascii_base - shift) % 26 + ascii_base)
            decrypted_chars.append(shifted_char)

            # Move to the next letter in the key, wrapping around if the key ends
            key_index = (key_index + 1) % key_length
        else:
            # Preserve special characters, numbers, spaces, and non-ASCII letters exactly as they are.
            # Notice that key_index is NOT incremented here, ensuring the key alignment is maintained.
            decrypted_chars.append(char)

    return "".join(decrypted_chars)


# ==========================================
# 2. EXECUTION
# ==========================================

if __name__ == "__main__":
    # Replace 'your_encrypted_text_here' with the actual ciphertext from the challenge.
    TARGET_CIPHERTEXT = "your_encrypted_text_here"

    # Replace 'your_key_here' with the keyword deduced or provided in the challenge.
    DECRYPTION_KEY = "your_key_here"

    if TARGET_CIPHERTEXT == "your_encrypted_text_here" or DECRYPTION_KEY == "your_key_here":
        print("Please replace 'TARGET_CIPHERTEXT' and 'DECRYPTION_KEY' with valid strings.")
    else:
        print("[*] Initiating Vigenère Cipher decryption...\n")
        plaintext = decrypt_vigenere(TARGET_CIPHERTEXT, DECRYPTION_KEY)
        print(f"[+] Decrypted text: {plaintext}")
