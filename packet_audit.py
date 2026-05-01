#!/usr/bin/env python3
"""
Bare-Bones Packet Auditor v1.1.2
Philosophy: Simple • Practical • Reliable
"""

import scapy.all as scapy
from scapy.layers.inet6 import ICMPv6EchoRequest
from datetime import datetime
import sys
import argparse
import platform

# =========================
# CONFIG & GLOBALS
# =========================
TOOL_VERSION = "1.1.2"
packet_count = 0
start_time = None
log_file = None
quiet_mode = False


def trunc(addr, width=39):
    """Truncate long addresses for terminal display."""
    return addr if len(addr) <= width else addr[:width - 3] + "..."


def audit_packet(packet):
    """Process and display packet metadata."""
    global packet_count, log_file, quiet_mode

    timestamp = datetime.now().strftime("%H:%M:%S")
    src = dst = "N/A"

    # ---- Handle IPv4 and IPv6 ----
    if packet.haslayer(scapy.IP):
        ip_layer = packet[scapy.IP]
        src, dst = ip_layer.src, ip_layer.dst

    elif packet.haslayer(scapy.IPv6):
        ip_layer = packet[scapy.IPv6]
        src, dst = ip_layer.src, ip_layer.dst

    else:
        return  # Skip non-IP packets

    # Count only displayed packets
    packet_count += 1

    # ---- Determine Layer 4 Protocol ----
    if packet.haslayer(scapy.TCP):
        tcp_layer = packet[scapy.TCP]
        flags = tcp_layer.sprintf("%TCP.flags%")
        transport_info = f"TCP {tcp_layer.sport}->{tcp_layer.dport} [{flags}]"

    elif packet.haslayer(scapy.UDP):
        udp_layer = packet[scapy.UDP]
        transport_info = f"UDP {udp_layer.sport}->{udp_layer.dport}"

    elif packet.haslayer(scapy.ICMP) or packet.haslayer(ICMPv6EchoRequest):
        transport_info = "ICMP"

    else:
        proto = getattr(ip_layer, "proto", getattr(ip_layer, "nh", "UNK"))
        transport_info = f"PROTO {proto}"

    # ---- Format Output ----
    output = (
        f"[{timestamp}] #{packet_count:<6} "
        f"{trunc(src):39} -> {trunc(dst):39} | "
        f"{transport_info[:25]:25} | {len(packet)} bytes"
    )

    # ---- Log to File ----
    if log_file:
        log_file.write(output + "\n")
        log_file.flush()

    # ---- Print to Terminal ----
    if not quiet_mode:
        print(output)


def main():
    global packet_count, start_time, log_file, quiet_mode

    packet_count = 0
    start_time = None

    # ---- Platform Check ----
    if "android" in platform.platform().lower() or "android" in platform.system().lower():
        print("[!] Android/Termux detected.")
        print("[!] Packet sniffing is not supported by Scapy on this platform.")
        print("[i] Use Linux/macOS/Windows with proper privileges.")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Bare-Bones Packet Auditor: Simple, Practical, Reliable",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-i", "--iface",
        help="Interface to sniff on"
    )

    parser.add_argument(
        "-f", "--filter",
        default="",
        help="BPF filter, e.g. 'tcp port 443'"
    )

    parser.add_argument(
        "-o", "--output",
        help="Save audit log to a text file"
    )

    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Quiet mode: suppress terminal packet output"
    )

    parser.add_argument(
        "-l", "--list-interfaces",
        action="store_true",
        help="List available interfaces and exit"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"PacketAuditor {TOOL_VERSION}"
    )

    args = parser.parse_args()
    quiet_mode = args.quiet

    # ---- List Interfaces ----
    if args.list_interfaces:
        print("Available interfaces:")
        for iface in scapy.get_if_list():
            default_marker = " (default)" if iface == scapy.conf.iface else ""
            print(f" - {iface}{default_marker}")
        sys.exit(0)

    # ---- Interface Selection ----
    iface = args.iface or scapy.conf.iface

    if not iface:
        print("[!] No valid interface found.")
        print("[i] Use -l to list interfaces.")
        sys.exit(1)

    # ---- Setup Logging ----
    if args.output:
        try:
            log_file = open(args.output, "a", buffering=1)

            if not quiet_mode:
                print(f"[i] Logging to: {args.output}")

        except Exception as e:
            print(f"[!] Could not open log file: {e}")
            sys.exit(1)

    # ---- Header ----
    if not quiet_mode:
        print(f"--- Bare-Bones Packet Auditor v{TOOL_VERSION} ---")
        print("Philosophy: Simple, Practical, Reliable")
        print(f"Interface: {iface}")

        if args.filter:
            print(f"Filter: {args.filter}")

        print("Monitoring traffic... Press Ctrl+C to stop.")

    # ---- Sniff Configuration ----
    sniff_args = {
        "prn": audit_packet,
        "store": 0
    }

    if iface:
        sniff_args["iface"] = iface

    if args.filter:
        sniff_args["filter"] = args.filter

    # ---- Start Timer ----
    start_time = datetime.now()

    # ---- Run Sniffer ----
    try:
        scapy.sniff(**sniff_args)

    except KeyboardInterrupt:
        duration = (datetime.now() - start_time).total_seconds()
        pps = packet_count / duration if duration > 0 else 0

        print("\n[!] Audit stopped by user.")
        print(f"[i] Packets: {packet_count} | Duration: {duration:.2f}s | Rate: {pps:.2f} pkt/s")
        sys.exit(0)

    except PermissionError:
        print("[!] Error: Root/Admin privileges required.")
        sys.exit(1)

    except OSError as e:
        if "No such device" in str(e):
            print(f"[!] Error: Interface '{iface}' not found.")
            print("[i] Use -l to list interfaces.")
        else:
            print(f"[!] OS Error: {e}")

        sys.exit(1)

    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        sys.exit(1)

    finally:
        if log_file:
            log_file.close()


if __name__ == "__main__":
    main()