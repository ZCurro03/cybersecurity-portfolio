"""
Interactive Monoalphabetic Substitution Decoder

This script provides an interactive command-line interface to manually decrypt
monoalphabetic substitution ciphers (cryptograms).

It dynamically replaces targeted encrypted characters with their plaintext
counterparts across the entire payload, allowing the analyst to perform
frequency analysis, syntax deduction, and pattern recognition on the fly.
Characters that have not yet been mapped are left in their original encrypted state.

Required Data:
- 'TARGET_CIPHERTEXT': The encrypted string you want to decode.

Generated Output:
The script prints the current state of the decrypted text to the console after
every substitution, updating the payload in real-time.
"""

def apply_substitutions(ciphertext, replacements):
    """
    Applies the current dictionary of character replacements to the ciphertext.
    Characters without a defined replacement remain unchanged, preserving
    uppercase formatting and special symbols by default.
    """

    decrypted_text = []
    for char in ciphertext:
        if char in replacements:
            decrypted_text.append(replacements[char])
        else:
            # Maintain the original character if no replacement is defined
            decrypted_text.append(char)

    return "".join(decrypted_text)


def interactive_decoder(ciphertext):
    """
    Main loop for the interactive decoding session. Prompts the user for
    character mappings and updates the payload state dynamically.
    """

    replacements = {}

    print("[*] Initiating Interactive Substitution Decoder...")

    while True:
        # Generate the current version of the text
        current_text = apply_substitutions(ciphertext, replacements)

        print("\n" + "="*60)
        print("CURRENT DECRYPTION STATE:")
        print("="*60)
        print(current_text)
        print("="*60)

        print("\n[Type 'exit' to terminate the program]")
        cipher_char = input("[?] Encrypted character to replace: ")

        if cipher_char.lower() == 'exit':
            print("\n[+] Decryption session terminated. Final text state preserved above.")
            break

        if len(cipher_char) != 1:
            print("[!] ERROR: Please enter exactly one character.")
            continue

        plain_char = input(f"[?] Plaintext character to substitute '{cipher_char}' with: ")

        if len(plain_char) != 1:
            print("[!] ERROR: Please enter exactly one character.")
            continue

        # Update the dictionary with the new character mapping
        replacements[cipher_char] = plain_char


if __name__ == "__main__":
    # Replace 'your_encrypted_text_here' with the actual ciphertext from the challenge.
    TARGET_CIPHERTEXT = "your_encrypted_text_here"

    if TARGET_CIPHERTEXT == "your_encrypted_text_here":
        print("Please replace 'TARGET_CIPHERTEXT' with a valid encrypted string.")
    else:
        interactive_decoder(TARGET_CIPHERTEXT)
