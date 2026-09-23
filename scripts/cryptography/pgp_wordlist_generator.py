"""
PGP Custom Wordlist Generator

This script generates a highly constrained custom password dictionary tailored for
targeted brute-force attacks. It computes permutations based on strict rules:
- Length must be exactly 6 or 7 characters.
- Characters are drawn from a restricted lowercase set ('qwertyiopnmjk').
- No character repetition is allowed.
- Passwords may contain either zero digits or exactly one digit from a restricted set ('013').

Required Data:
- The constants 'LETTERS', 'DIGITS', and 'SIZES' dictate the generation rules.
- 'OUTPUT_FILE': The destination path for the generated wordlist.

Generated Output:
A plain text file containing all valid password combinations (one per line),
ready to be ingested by tools like GnuPG, Hashcat, or John The Ripper.
"""

import itertools

# ==========================================
# 1. GENERATION LOGIC
# ==========================================

def generate_dictionary(output_filepath):
    """
    Computes and writes all valid password permutations to disk.
    It uses itertools to avoid loading all 38+ million combinations into RAM,
    writing them sequentially to the file buffer instead.
    """

    # Character sets extracted from the challenge constraints
    LETTERS = "qwertyiopnmjk"
    DIGITS = "013"
    SIZES = [6, 7]

    print(f"[*] Generating constrained wordlist to: {output_filepath}")
    print("[*] This may take a few moments due to the high number of permutations...")

    with open(output_filepath, "w") as f:
        for size in SIZES:
            # Step 1: Generate passwords containing ONLY letters
            # itertools.permutations generates all unique orderings of the specified length
            for combo in itertools.permutations(LETTERS, size):
                f.write("".join(combo) + "\n")

            # Step 2: Generate passwords containing EXACTLY ONE digit
            for digit in DIGITS:
                # We need (size - 1) letters to complete the required length
                for letter_combo in itertools.combinations(LETTERS, size - 1):
                    # Combine the selected letters with the current digit
                    char_set = list(letter_combo) + [digit]

                    # Generate all possible positional orderings for this specific character set
                    for perm in itertools.permutations(char_set):
                        f.write("".join(perm) + "\n")

    print("[+] Wordlist generation complete.")


# ==========================================
# 2. EXECUTION
# ==========================================

if __name__ == "__main__":
    # Target output file. Ensure sufficient disk space (file may be several hundred MBs).
    OUTPUT_FILE = "challenge_dictionary.txt"

    generate_dictionary(OUTPUT_FILE)
