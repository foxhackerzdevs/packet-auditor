# 📡 Bare-Bones Packet Auditor v1.1.1

**Philosophy:** *Simple • Practical • Reliable*

A lightweight command-line network packet auditing tool built with Python and Scapy. It captures live network traffic and displays concise, human-readable metadata in real time.

---

## 📖 Introduction

**Bare-Bones Packet Auditor** is designed for developers, students, and security enthusiasts who need a minimal yet effective way to observe network traffic.

It prioritizes:

* clarity
* performance
* usability

No unnecessary complexity — just useful output.

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

---

### Option 2: Clone and run manually

```bash
git clone https://github.com/foxhackerzdevs/packet-auditor.git
cd packet-auditor
pip install .
```

---

> ⚠️ Root/Admin privileges are required for packet sniffing.

---

## 🚀 Usage

### After pip install (CLI command)

```bash
sudo packet-audit
```

---

### Options

| Option                    | Description                                                       |
| ------------------------- | ----------------------------------------------------------------- |
| `-i`, `--iface`           | Network interface to sniff on (default: system default interface) |
| `-f`, `--filter`          | BPF filter string (e.g., `"tcp port 443"`)                        |
| `-o`, `--output`          | Save output to a log file                                         |
| `-q`, `--quiet`           | Disable terminal output (use with logging)                        |
| `-l`, `--list-interfaces` | List available interfaces and exit                                |
| `--version`               | Display tool version                                              |

---

## ✨ Features

* 📦 Real-time packet monitoring
* 🌐 IPv4 and IPv6 support
* 🔍 TCP, UDP, ICMP detection
* 🧠 TCP flag inspection
* ⚡ Lightweight (`store=0`, no memory buildup)
* 🎯 BPF filtering support
* 📁 Optional logging to file
* 🤫 Quiet mode for background operation
* 🖥️ Clean, aligned terminal output

---

## 📦 Dependencies

Defined in `pyproject.toml`:

* `scapy >= 2.5.0`

---

## 🔧 Configuration

No configuration file required. Everything is controlled via CLI arguments.

---

## 📊 Output Format

```text
[HH:MM:SS] #COUNT SOURCE_IP -> DESTINATION_IP | PROTOCOL INFO | SIZE bytes
```

### Example:

```text
[12:34:56] #42     192.168.1.10 -> 142.250.183.78 | TCP 443->51532 [S] | 60 bytes
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

# Log to file
sudo packet-audit -o packets.log

# Quiet background logging
sudo packet-audit -q -o packets.log

# Combined usage
sudo packet-audit -i wlan0 -f "host 8.8.8.8" -o log.txt
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
packet-audit -l
```

---

### ❌ No Packets Captured

Possible causes:

* Wrong interface
* Overly strict filter
* No active network traffic

---

### ❌ Android / Termux Not Supported

Packet sniffing is not supported on Android due to OS limitations.

Use Linux or macOS instead.

---

## 👥 Contributors

* **Abhrankan Chakrabarti** ([@Abhrankan-Chakrabarti](https://github.com/Abhrankan-Chakrabarti))
* Maintained via **foxhackerzdevs**

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Notes

* Designed for learning, debugging, and lightweight monitoring
* Not a full intrusion detection system
* Use only on networks you own or are authorized to monitor
