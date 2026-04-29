# 📡 Bare-Bones Packet Auditor v1.1

**Philosophy:** *Simple • Practical • Reliable*

A lightweight command-line network packet auditing tool built with Python and Scapy. It captures live network traffic and displays concise, human-readable metadata for each packet in real time.

---

## 📖 Introduction

**Bare-Bones Packet Auditor** is designed for developers, students, and security enthusiasts who need a minimal yet effective way to observe network traffic.

---

## 📚 Table of Contents

* [Introduction](#-introduction)
* [Installation](#%EF%B8%8F-installation)
* [Usage](#-usage)
* [Features](#-features)
* [Dependencies](#-dependencies)
* [Configuration](#-configuration)
* [Output Format](#-output-format)
* [Examples](#-examples)
* [Troubleshooting](#-troubleshooting)
* [Contributors](#-contributors)
* [License](#-license)

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/foxhackerzdevs/packet-auditor.git
cd packet-auditor
```

### 2. Install Dependencies

```bash
pip install scapy
```

### 3. Run the Script

```bash
python3 packet_audit.py
```

> ⚠️ Root/Admin privileges are required for packet sniffing.

---

## 🚀 Usage

```bash
sudo python3 packet_audit.py [OPTIONS]
```

### Options:

| Option           | Description                   |
| ---------------- | ----------------------------- |
| `-i`, `--iface`  | Network interface to sniff on |
| `-f`, `--filter` | BPF filter string             |
| `--version`      | Display tool version          |

---

## ✨ Features

* Real-time packet monitoring
* IPv4 and IPv6 support
* TCP, UDP, ICMP detection
* TCP flags visibility
* Memory-efficient (`store=0`)
* BPF filtering support
* Clean terminal output

---

## 📦 Dependencies

* Python 3.x
* Scapy

---

## 🔧 Configuration

No configuration file required.

---

## 📊 Output Format

```text
[HH:MM:SS] SOURCE_IP -> DESTINATION_IP | PROTOCOL INFO | PACKET_SIZE bytes
```

---

## 🧪 Examples

```bash
sudo python3 packet_audit.py
sudo python3 packet_audit.py -i eth0
sudo python3 packet_audit.py -f "tcp port 80"
```

---

## 🛠️ Troubleshooting

* Use `sudo` if permission denied
* Check interfaces with `ip link show`
* Ensure network activity exists

---

## 👥 Contributors

* **Abhrankan Chakrabarti** ([@Abhrankan-Chakrabarti](https://github.com/Abhrankan-Chakrabarti))
* Maintained via **foxhackerzdevs**

---

## 📄 License

MIT License
