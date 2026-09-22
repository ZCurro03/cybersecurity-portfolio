# 🛡️  Cybersecurity Portfolio

Welcome to my personal cybersecurity and threat hunting challenge portfolio.

> ⚠️  **Ethics & Policy Note:** In strict compliance with platforms like **Atenea (CCN-CERT)**, this repository **does not contain flags, passwords, or step-by-step write-ups**. Its purpose is to serve as a technical log of acquired cybersecurity concepts and automated analysis tools.

## 🛠️  Technical Arsenal

* Network Analysis: Wireshark, Tshark.
* Malware Forensics: Cobalt Strike configuration extraction, Malleable C2 profile analysis.
* Cryptography: RSA/AES decryption.
* Development: Python (cryptography integration, binary parsing).

## 🚩 Solved Challenges

### 🏛️  Platform: CCN-CERT Atenea

| Challenge | Category | Applied Skills & Concepts | Tools Used |
|-|-|-|-|
| Kobaloi | Traffic Analysis | <ul><li>Detection of beaconing behavior and Command & Control (C2) channels.</li><li>Extraction and de-obfuscation of payloads hidden inside fake HTTP traffic (Malleable C2 profiles mimicking jQuery).</li><li>Cryptographic analysis of Cobalt Strike payloads, recovering public keys, and decrypting AES-256 traffic using leaked RSA private keys via OSINT.</li> | Wireshark, Tshark, `1768.py`, Python (`PyCryptodome`) |

## 💻 Custom Tooling & Scripts

* `cobalt_strike_beacon_parser.py`: Custom script utilizing asymmetric and symmetric cryptographic routines to process encrypted exfiltrated session logs and network POST dumps.
