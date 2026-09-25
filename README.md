# 🛡️  Cybersecurity Portfolio

Welcome to my personal cybersecurity and threat hunting challenge portfolio.

> ⚠️  **Ethics & Policy Note:** In strict compliance with platforms like **Atenea (CCN-CERT)**, this repository **does not contain flags, passwords, or step-by-step write-ups**. Its purpose is to serve as a technical log of acquired cybersecurity concepts and automated analysis tools.

## 🛠️  Technical Arsenal

* Network Analysis: Wireshark, Tshark.
* Web Exploitation: Directory fuzzing, HTTP traffic interception (Burp Suite), JWT manipulation/forgery, and REST API reconnaissance & logic abuse (SwaggerUI).
* Malware Forensics: Cobalt Strike configuration extraction, Malleable C2 profile analysis.
* Cryptography & Steganography: RSA/AES decryption, block cipher cryptanalysis (Known-Plaintext Attacks), exploitation of structural vulnerabilities, classical polyalphabetic ciphers and OpenSSL payload decryption.
* Steganography: Metadata extraction, esoteric cipher analysis, audio forensics and spectrogram analysis.
* Development: Python (cryptography integration, binary parsing, algorithmic automation of classical ciphers).
* OSINT & GeoINT: Reverse image searching, geospatial analysis, and Street View reconnaissance.
* Forensics (Linux): Firmware analysis, embedded filesystem extraction (SquashFS), and system credential forensics.
* Forensics (Windows): Disk image processing (Autopsy), artifact analysis (malicious .lnk shortcuts, hidden executables), and triage of obfuscated Command & Control droppers.
* Password Cracking: Hash extraction from compressed archives and offline brute-forcing.

## 🚩 Solved Challenges

### 🏛️  Platform: CCN-CERT Atenea

| Challenge | Category | Applied Skills & Concepts | Tools Used |
|-|-|-|-|
| Kobaloi | Traffic Analysis | <ul><li>Detection of beaconing behavior and Command & Control (C2) channels.</li><li>Extraction and de-obfuscation of payloads hidden inside fake HTTP traffic (Malleable C2 profiles mimicking jQuery).</li><li>Cryptographic analysis of Cobalt Strike payloads, recovering public keys, and decrypting AES-256 traffic using leaked RSA private keys via OSINT.</li></ul> | Wireshark, Tshark, `1768.py`, Python (`PyCryptodome`) |
| APT GeoGuesser | OSINT / GeoINT | <ul><li>Video forensics to extract key frames and identify unique environmental markers.</li><li>Reverse image search to narrow down geographical candidate locations.</li><li>First-person geospatial analysis to visually verify architectural and urban elements against the video evidence.</li></ul> | Google Lens, Google Maps (Street View) |
| Rabid Gruya | OSINT / GeoINT | <ul><li>Geospatial reconnaissance based on video recordings.</li><li>Utilization of reverse image search to pinpoint specific cities or regions.</li><li>Manual navigation and verification of terrain layout using first-person mapping tools.</li></ul> | Google Lens, Google Maps (Street View) |
| Oldtimes | Steganography | <ul><li>Metadata extraction and analysis from image files (JPEG).</li><li>Decoding of Base64 strings embedded in EXIF data and conversion to raw hexadecimal format.</li><li>Pattern recognition and resolution of esoteric/legacy ciphers (translating hex values into Multi-tap legacy telephone keypad sequences).</li></ul> | exiftool, CyberChef |
| Covert | Steganography | <ul><li>Audio forensics applied to multimedia files (video audio tracks).</li><li>Frequency analysis and anomaly detection within audio signals.</li><li>Extraction of hidden textual information through visual spectrogram representation.</li></ul> | Wavacity |
| Mad Max | Steganography | <ul><li>Extraction of password hashes from compressed archives and offline cracking.</li><li>Multimedia metadata analysis to discover contextual passwords.</li><li>Audio forensics and hidden data extraction using specialized password-protected steganography tools.</li></ul> | exiftool, 7z2john, hashcat, DeepSound |
| Don't Roll Your Own Crypto | Cryptography / Steganography | <ul><li>Exploitation of structural weaknesses in custom cryptographic implementations (Linear modified SBOX).</li><li>Block cipher cryptanalysis (AES-128-CBC) allowing block-by-block decryption without key extraction.</li><li>Known-plaintext attack utilizing file format signatures (PNG magic bytes) to deduce cryptographic masks.</li></ul> | Python (Custom Script) |
| Got Cloudy | Web Exploitation | <ul><li>Directory fuzzing and reconnaissance to discover hidden endpoints.</li><li>HTTP traffic interception to capture and analyze transient session cookies (HttpOnly;Secure).</li><li>Cryptographic analysis of JSON Web Tokens (JWT), offline secret brute-forcing, and token forgery to escalate privileges.</li></ul> | ffuf, Burp Suite, jwt.io, Python (Custom Scripts) |
| R'lyeh | Web Exploitation | <ul><li>Discovery of exposed environment configuration files via directory fuzzing to extract database credentials.</li><li>API endpoint reconnaissance and interaction using SwaggerUI documentation.</li><li>Identification of weak, deterministic token generation mechanisms.</li><li>Privilege escalation to moderator level by forging tokens using leaked user attributes from various API endpoints.</li></ul> | Burp Suite, CyberChef |
| Tattoo | Forensics | <ul><li>Embedded filesystem analysis and artifact extraction from raw USB disk images.</li><li>Triage of initial access payloads and discarding of decoy documents.</li><li>Forensic analysis of malicious Windows Shortcuts (.lnk).</li><li>Deobfuscation of evasion-oriented Batch scripts via environmental variable substring indexing to extract Command & Control (C2) domains.</li></ul> | file, binwalk, Autopsy |

#### 2018 Challenges

| Challenge | Category | Applied Skills & Concepts | Tools Used |
|-|-|-|-|
| Ave César! | Cryptography | <ul><li>Cryptanalysis and resolution of classical substitution ciphers.</li><li>Development of custom automation to brute-force shift keys.</li><li>Algorithm design to preserve data integrity (case sensitivity and special characters) during decryption.</li></ul> | Python (Custom Script) |
| Vigenere | Cryptography | <ul><li>Cryptanalysis of polyalphabetic substitution ciphers (Vigènere).</li><li>Application of frequency analysis and Kasiski examination concepts to deduce key length.</li><li>Contextual brute-forcing using custom wordlists derived from challenge metadata to recover the decryption key.</li><li>Development of custom scripts to automate dynamic keyword scheduling and shifting.</li><li>Algorithm design to preserve payload formatting, bypassing special and non-ASCII characters without disrupting the key index.</li></ul> | Guballa Vigenère Solver, Python (Custom Script) |
| Podrías descifrar el mensaje sin la clave? | Cryptography | <ul><li>Cryptanalysis and resolution of monoalphabetic substitution ciphers.</li><li>Application of manual frequency analysis and pattern recognition in natural language texts.</li><li>Development of interactive cryptographic tooling for real-time payload substitution.</li></ul> | Python (Custom Script) |
| Durin's Gates | Steganography / Cryptography | <ul><li>Contextual OSINT research to deduce steganographic passphrases from pop culture references.</li><li>Steganographic data extraction from multimedia files to recover external payloads.</li><li>Multimedia metadata forensics (EXIF analysis) to discover cryptographic keys.</li><li>Decoding of Base64 streams and decryption of OpenSSL payloads (AES-256-CBC) to recover embedded video files.</li></ul> | steghide, exiftool, OpenSSL, CyberChef |
| Really??? | Steganography / Cryptography | <ul><li>Development of combinatorial algorithms to generate highly constrained, rules-based custom password dictionaries.</li><li>Automation of PGP symmetric decryption brute-forcing via shell scripting.</li><li>Detection and extraction of whitespace steganography (Stegsnow) hidden within decrypted plaintext payloads.</li></ul> | Python (Custom Script), Bash (Custom Script), GnuPG, stegsnow |
| Juegos de guerra | Steganography / GeoINT | <ul><li>Iterative extraction of embedded thumbnail payloads from multimedia files.</li><li>Metadata forensics (EXIF analysis) to recover fragmented geospatial coordinates (Latitude/Longitude).</li><li>Geospatial intelligence and satellite imagery analysis to visually locate physical ground markings.</li></ul> | exiftool, Google Maps (Satellite) |
| Hurgando en el router | Forensics | <ul><li>Firmware analysis and automated extraction of embedded filesystems (SquashFS).</li><li>Identification and extraction of Linux system credential files (/etc/shadow).</li><li>Offline password cracking using dictionary attacks against SHA-512 crypt hashes.</li></ul> | binwalk, hashcat |

## 💻 Custom Tooling & Scripts

### 🧩 Cryptography

* `custom_aes_sbox_decryptor.py`: Python script designed to bypass AES-128-CBC chaining and deduce key masks via known-plaintext attacks on custom linear SBOXes.
* `caesar_cipher_bruteforcer.py`: Generic cryptographic tool to automate brute-force decryption of Caesar substitution ciphers while preserving uppercase, lowercase, and special character formatting.
* `vigenere_cipher_decoder.py`: Cryptographic tool designed to decode Vigenère polyalphabetic ciphers dynamically, preserving uppercase, lowercase, special characters, and non-ASCII symbols without misaligning the keyword index.
* `interactive_substitution_decoder.py`: Interactive cryptographic tool designed to assist in the manual decryption of monoalphabetic substitution ciphers through real-time character mapping.
* `pgp_wordlist_generator.py`: Python script utilizing the `itertools` library to generate massive, highly-constrained permutation dictionaries based on specific character sets, lengths, and digit-inclusion rules.
* `pgp_symmetric_bruteforcer.sh`: Bash automation script designed to loop through custom dictionaries and brute-force PGP symmetrically encrypted payloads silently and efficiently.

### 🌐 Web Exploitation

* `jwt_secret_bruteforcer.py`: Custom script to perform offline brute-force attacks against JWT HMAC signatures using custom wordlists.
* `jwt_token_forger.py`: Cryptographic tool designed to generate and sign custom JSON Web Tokens (JWT) for privilege escalation using recovered secrets.

### 🔬 Malware forensics

* `cobalt_strike_beacon_parser.py`: Custom script utilizing asymmetric and symmetric cryptographic routines to process encrypted exfiltrated session logs and network POST dumps.
