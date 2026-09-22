# 🛡️  Cybersecurity Portfolio

Welcome to my personal cybersecurity and threat hunting challenge portfolio.

> ⚠️  **Ethics & Policy Note:** In strict compliance with platforms like **Atenea (CCN-CERT)**, this repository **does not contain flags, passwords, or step-by-step write-ups**. Its purpose is to serve as a technical log of acquired cybersecurity concepts and automated analysis tools.

## 🛠️  Technical Arsenal

* Network Analysis: Wireshark, Tshark.
* Malware Forensics: Cobalt Strike configuration extraction, Malleable C2 profile analysis.
* Cryptography: RSA/AES decryption.
* Development: Python (cryptography integration, binary parsing).
* OSINT & GeoINT: Reverse image searching, geospatial analysis, and Street View reconnaissance.

## 🚩 Solved Challenges

### 🏛️  Platform: CCN-CERT Atenea

| Challenge | Category | Applied Skills & Concepts | Tools Used |
|-|-|-|-|
| Kobaloi | Traffic Analysis | <ul><li>Detection of beaconing behavior and Command & Control (C2) channels.</li><li>Extraction and de-obfuscation of payloads hidden inside fake HTTP traffic (Malleable C2 profiles mimicking jQuery).</li><li>Cryptographic analysis of Cobalt Strike payloads, recovering public keys, and decrypting AES-256 traffic using leaked RSA private keys via OSINT.</li></ul> | Wireshark, Tshark, `1768.py`, Python (`PyCryptodome`) |
| APT GeoGuesser | OSINT / GeoINT | <ul><li>Video forensics to extract key frames and identify unique environmental markers.</li><li>Reverse image search to narrow down geographical candidate locations.</li><li>First-person geospatial analysis to visually verify architectural and urban elements against the video evidence.</li></ul> | Google Lens, Google Maps (Street View) |
| Rabid Gruya | OSINT / GeoINT | <ul><li>Geospatial reconnaissance based on video recordings.</li><li>Utilization of reverse image search to pinpoint specific cities or regions.</li><li>Manual navigation and verification of terrain layout using first-person mapping tools.</li></ul> | Google Lens, Google Maps (Street View) |

## 💻 Custom Tooling & Scripts

* `cobalt_strike_beacon_parser.py`: Custom script utilizing asymmetric and symmetric cryptographic routines to process encrypted exfiltrated session logs and network POST dumps.
