# 📡 Bare-Bones Packet Auditor v1.1

**Philosophy:** *Simple • Practical • Reliable*

A lightweight command-line network packet auditing tool built with Python and Scapy. It captures live network traffic and displays concise, human-readable metadata for each packet in real time.

---

## 📖 Introduction

**Bare-Bones Packet Auditor** is designed for developers, students, and security enthusiasts who need a minimal yet effective way to observe network traffic. It focuses on clarity and performance, avoiding unnecessary complexity while still supporting essential packet inspection features.

---

## 📚 Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Dependencies](#dependencies)
* [Configuration](#configuration)
* [Output Format](#output-format)
* [Examples](#examples)
* [Troubleshooting](#troubleshooting)
* [Contributors](#contributors)
* [License](#license)

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

* Python 3.x
* Scapy

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
sudo python3 packet_audit.py

# Specific interface
sudo python3 packet_audit.py -i eth0

# Filtered traffic
sudo python3 packet_audit.py -f "tcp port 80"

# Combined
sudo python3 packet_audit.py -i wlan0 -f "host 8.8.8.8"
```

---

## 🛠️ Troubleshooting

### ❌ Permission Denied

Run with:

```bash
sudo python3 packet_audit.py
```

### ❌ Interface Not Found

```bash
ip link show
```

### ❌ No Packets Captured

* Wrong interface
* Overly strict filter
* No active traffic

---

## 👥 Contributors

* **Abhrankan Chakrabarti** ([@Abhrankan-Chakrabarti](https://github.com/Abhrankan-Chakrabarti))
* Project maintained via **foxhackerzdevs** GitHub account

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Notes

* Designed for educational and debugging purposes
* Not intended as a full intrusion detection system
* Use only on networks you own or are authorized to monitor
