"""
Caesar Cipher Brute-Forcer

This script automates the decryption of classical Caesar substitution ciphers.
Since the exact shift key is often unknown in CTF environments, this tool performs a
brute-force attack, generating all 25 possible plaintext variations.

It is specifically designed to preserve the original formatting of the payload,
dynamically maintaining uppercase letters, lowercase letters, and bypassing
special characters, numbers, and non-ASCII characters (such as Spanish accented
vowels or 'ñ') without altering them.

Required Data:
- 'TARGET_CIPHERTEXT': The encrypted string you want to decode.

Generated Output:
The script prints all 25 possible shifted plaintexts to the console, allowing the
analyst to visually identify the correct flag or readable text.
"""

# ==========================================
# 1. ALGORITHM IMPLEMENTATION
# ==========================================

def decrypt_caesar(ciphertext, shift):
    """
    Applies a reverse Caesar cipher shift to a given string.
    Uses modulo 26 arithmetic to wrap around the standard alphabet properly.
    """

    decrypted_chars = []
    
    for char in ciphertext:
        # Check if the character is a standard ASCII letter (a-z, A-Z).
        # Non-ASCII letters like 'á', 'ñ', or 'ü' will bypass this block.
        if char.isalpha() and char.isascii():
            # Determine the ASCII base depending on whether the letter is upper or lower case
            ascii_base = ord('A') if char.isupper() else ord('a')
            
            # 1. Normalize the character to a 0-25 range (ord(char) - ascii_base).
            # 2. Subtract the shift key to decrypt.
            # 3. Apply modulo 26 to handle alphabet wrap-around (e.g., 'A' shifted back becomes 'Z').
            # 4. Add the base back to get the final readable ASCII character.
            shifted_char = chr((ord(char) - ascii_base - shift) % 26 + ascii_base)
            decrypted_chars.append(shifted_char)
        else:
            # Preserve special characters, numbers, spaces, and non-ASCII letters exactly as they are
            decrypted_chars.append(char)
            
    return "".join(decrypted_chars)


# ==========================================
# 2. BRUTE-FORCE EXECUTION
# ==========================================

def brute_force_caesar(ciphertext):
    """
    Iterates through all 25 possible Caesar cipher shifts and prints the results.
    """

    print("[*] Initiating Caesar Cipher brute-force attack...\n")
    
    # A standard Caesar cipher has 25 possible shifts (26 would result in the same ciphertext)
    for shift_key in range(1, 26):
        plaintext = decrypt_caesar(ciphertext, shift_key)
        # Format the output with a fixed width for the shift key to keep the console clean
        print(f"[+] Shift {shift_key:02d}: {plaintext}")
        
    print("\n[*] Brute-force complete. Manually review the output for readable text or flags.")


if __name__ == "__main__":
    # Replace 'your_encrypted_text_here' with the actual ciphertext from the challenge.
    # Example: "Uijt jt b tfdsfu nfttbhf!"
    TARGET_CIPHERTEXT = "your_encrypted_text_here"

    if TARGET_CIPHERTEXT == "your_encrypted_text_here":
        print("Please replace 'TARGET_CIPHERTEXT' with a valid encrypted string.")
    else:
        brute_force_caesar(TARGET_CIPHERTEXT)
