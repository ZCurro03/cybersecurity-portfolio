# 🛡️  Cybersecurity Portfolio

Welcome to my personal cybersecurity and threat hunting challenge portfolio.

> ⚠️  **Ethics & Policy Note:** In strict compliance with platforms like **Atenea (CCN-CERT)**, this repository **does not contain flags, passwords, or step-by-step write-ups**. Its purpose is to serve as a technical log of acquired cybersecurity concepts and automated analysis tools.

## 🛠️  Technical Arsenal

* Network Analysis: Wireshark, Tshark.
* Malware Forensics: Cobalt Strike configuration extraction, Malleable C2 profile analysis.
* Cryptography: RSA/AES decryption, block cipher cryptanalysis (Known-Plaintext Attacks) and exploitation of structural vulnerabilities in custom cryptography.
* Steganography: metadata extraction, esoteric cipher analysis, audio forensics and spectrogram analysis.
* Development: Python (cryptography integration, binary parsing).
* OSINT & GeoINT: Reverse image searching, geospatial analysis, and Street View reconnaissance.
* Password Cracking: Hash extraction from compressed archives and offline brute-forcing.

## 🚩 Solved Challenges

### 🏛️  Platform: CCN-CERT Atenea

| Challenge | Category | Applied Skills & Concepts | Tools Used |
|-|-|-|-|
| Kobaloi | Traffic Analysis | <ul><li>Detection of beaconing behavior and Command & Control (C2) channels.</li><li>Extraction and de-obfuscation of payloads hidden inside fake HTTP traffic (Malleable C2 profiles mimicking jQuery).</li><li>Cryptographic analysis of Cobalt Strike payloads, recovering public keys, and decrypting AES-256 traffic using leaked RSA private keys via OSINT.</li></ul> | Wireshark, Tshark, `1768.py`, Python (`PyCryptodome`) |
| APT GeoGuesser | OSINT / GeoINT | <ul><li>Video forensics to extract key frames and identify unique environmental markers.</li><li>Reverse image search to narrow down geographical candidate locations.</li><li>First-person geospatial analysis to visually verify architectural and urban elements against the video evidence.</li></ul> | Google Lens, Google Maps (Street View) |
| Rabid Gruya | OSINT / GeoINT | <ul><li>Geospatial reconnaissance based on video recordings.</li><li>Utilization of reverse image search to pinpoint specific cities or regions.</li><li>Manual navigation and verification of terrain layout using first-person mapping tools.</li></ul> | Google Lens, Google Maps (Street View) |
| Oldtimes | Steganography | <ul><li>Metadata extraction and analysis from image files (JPEG).</li><li>Decoding of Base64 strings embedded in EXIF data and conversion to raw hexadecimal format.</li><li>Pattern recognition and resolution of esoteric/legacy ciphers (translating hex values into Multi-tap legacy telephone keypad sequences).</li></ul> | CyberChef |
| Covert | Steganography | <ul><li>Audio forensics applied to multimedia files (video audio tracks).</li><li>Frequency analysis and anomaly detection within audio signals.</li><li>Extraction of hidden textual information through visual spectrogram representation.</li></ul> | Wavacity |
| Mad Max | Steganography | <ul><li>Extraction of password hashes from compressed archives and offline cracking.</li><li>Multimedia metadata analysis to discover contextual passwords.</li><li>Audio forensics and hidden data extraction using specialized password-protected steganography tools.</li></ul> | 7z2john, hashcat, DeepSound |
| Don't Roll Your Own Crypto | Cryptography / Steganography | <ul><li>Exploitation of structural weaknesses in custom cryptographic implementations (Linear modified SBOX).</li><li>Block cipher cryptanalysis (AES-128-CBC) allowing block-by-block decryption without key extraction.</li><li>Known-plaintext attack utilizing file format signatures (PNG magic bytes) to deduce cryptographic masks.</li></ul> | Python (Custom Script) |

## 💻 Custom Tooling & Scripts

* `cobalt_strike_beacon_parser.py`: Custom script utilizing asymmetric and symmetric cryptographic routines to process encrypted exfiltrated session logs and network POST dumps.
* `custom_aes_sbox_decryptor.py`: Python script designed to bypass AES-128-CBC chaining and deduce key masks via known-plaintext attacks on custom linear SBOXes.
