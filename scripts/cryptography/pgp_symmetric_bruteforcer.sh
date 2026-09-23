#!/bin/bash
#
# PGP Symmetric Decryption Brute-Forcer
#
# This script automates the brute-forcing of PGP files symmetrically encrypted (AES, CAST5, etc.).
# It reads a provided dictionary line by line and attempts decryption using GnuPG.
# Output and errors are piped to /dev/null to maintain a clean terminal, halting
# execution immediately once the correct passphrase yields a successful exit code (0).

echo "[*] Initiating PGP brute-force attack..."

# ------------------------------------------
# CONFIGURATION VARIABLES
# ------------------------------------------
# Replace 'challenge_dictionary.txt' with the path to your generated wordlist
DICTIONARY="challenge_dictionary.txt"

# Replace 'target_file.asc' with the actual PGP encrypted file from the challenge
PGP_FILE="target_file.asc"

# Destination for the decrypted payload once the attack succeeds
OUTPUT_FILE="decrypted_payload.txt"


# ------------------------------------------
# VALIDATION
# ------------------------------------------
if [ ! -f "$DICTIONARY" ]; then
    echo "[!] Error: Dictionary file '$DICTIONARY' not found."
    exit 1
fi

if [ ! -f "$PGP_FILE" ]; then
    echo "[!] Error: Target PGP file '$PGP_FILE' not found."
    exit 1
fi


# ------------------------------------------
# ATTACK LOOP
# ------------------------------------------
# Read the dictionary strictly line by line (IFS= prevents whitespace trimming issues)
while IFS= read -r password; do

    # Execute GPG decryption silently:
    # --batch --yes: Prevents interactive prompts or overwriting confirmations
    # --pinentry-mode loopback: Forces GPG to take the passphrase from the command line argument
    gpg --batch --yes --pinentry-mode loopback --passphrase "$password" --output "$OUTPUT_FILE" --decrypt "$PGP_FILE" &>/dev/null

    # Check if the previous GPG command executed successfully (Exit Code 0 means decryption worked)
    if [ $? -eq 0 ]; then
        echo -e "\n========================================="
        echo "[+] PASSPHRASE FOUND: $password"
        echo "========================================="
        echo "[+] The file has been successfully decrypted and saved as '$OUTPUT_FILE'"
        # Break the loop immediately to stop testing passwords
        break
    fi

done < "$DICTIONARY"

echo "[*] Brute-force routine finished."
