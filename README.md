# 📡 Bare-Bones Packet Auditor v1.1

**Philosophy:** *Simple • Practical • Reliable*

A lightweight command-line network packet auditing tool built with Python and Scapy. It captures live network traffic and displays concise, human-readable metadata for each packet in real time.

---

## 📖 Introduction

**Bare-Bones Packet Auditor** is designed for developers, students, and security enthusiasts who need a minimal yet effective way to observe network traffic. It focuses on clarity and performance, avoiding unnecessary complexity while still supporting essential packet inspection features.

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
* [Troubleshooting](#%EF%B8%8F-troubleshooting)
* [Contributors](#-contributors)
* [License](#-license)

---

## ⚙️ Installation

### Option 1: Install via pip (recommended)

```bash
pip install packet-auditor
```

Or install locally from source:

```bash
pip install .
```

---

### Option 2: Clone and run manually

```bash
git clone https://github.com/foxhackerzdevs/packet-auditor.git
cd packet-auditor
pip install -r requirements.txt
```

---

> ⚠️ Root/Admin privileges are required for packet sniffing.

---

## 🚀 Usage

### After pip install (CLI command)

```bash
sudo packet-audit
```

### Direct Python execution

```bash
sudo python3 packet_audit.py
```

### Options:

| Option           | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| `-i`, `--iface`  | Network interface to sniff on (default: all interfaces)     |
| `-f`, `--filter` | BPF filter string (e.g., `"tcp port 443 and host 1.1.1.1"`) |
| `--version`      | Display tool version                                        |

---

## ✨ Features

* 📦 Real-time packet monitoring
* 🌐 Supports both IPv4 and IPv6
* 🔍 Layer 4 protocol detection (TCP, UDP, ICMP)
* 🧠 Displays TCP flags for deeper insight
* ⚡ Lightweight and memory-efficient (`store=0`)
* 🎯 Supports BPF filtering for targeted sniffing
* 🖥️ Clean, aligned terminal output

---

## 📦 Dependencies

Defined in `pyproject.toml`:

* `scapy >= 2.5.0`

---

## 🔧 Configuration

No configuration file required. All options are passed via CLI arguments.

---

## 📊 Output Format

```text
[HH:MM:SS] SOURCE_IP -> DESTINATION_IP | PROTOCOL INFO | PACKET_SIZE bytes
```

### Example:

```text
[12:34:56] 192.168.1.10 -> 142.250.183.78 | TCP 443->51532 [S] | 60 bytes
```

---

## 🧪 Examples

```bash
# Monitor all traffic
sudo packet-audit

# Specific interface
sudo packet-audit -i eth0

# Filtered traffic
sudo packet-audit -f "tcp port 80"

# Combined
sudo packet-audit -i wlan0 -f "host 8.8.8.8"
```

---

## 🛠️ Troubleshooting

### ❌ Permission Denied

```bash
sudo packet-audit
```

---

### ❌ Interface Not Found

```bash
ip link show
```

---

### ❌ No Packets Captured

* Wrong interface
* Overly strict filter
* No active traffic

---

## 👥 Contributors

* **Abhrankan Chakrabarti** ([@Abhrankan-Chakrabarti](https://github.com/Abhrankan-Chakrabarti))
* Maintained via **foxhackerzdevs**

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Notes

* Designed for educational and debugging purposes
* Not intended as a full intrusion detection system
* Use only on networks you own or are authorized to monitor
