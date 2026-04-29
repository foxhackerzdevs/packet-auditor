#!/usr/bin/env python3
"""
Bare-Bones Packet Auditor v1.1
Philosophy: Simple • Practical • Reliable
"""
import scapy.all as scapy
from datetime import datetime
import sys
import argparse

# =========================
# CONFIG
# =========================
TOOL_VERSION = "1.1"

def audit_packet(packet):
    """Callback function to process and display packet metadata."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    src = dst = "N/A"
    transport_info = "NON-IP"

    # Handle IPv4 and IPv6
    if packet.haslayer(scapy.IP):
        ip_layer = packet[scapy.IP]
        src, dst = ip_layer.src, ip_layer.dst
    elif packet.haslayer(scapy.IPv6):
        ip_layer = packet[scapy.IPv6]
        src, dst = ip_layer.src, ip_layer.dst
    else:
        return # Skip non-IP packets like ARP

    # Determine Layer 4 Protocol and Ports
    if packet.haslayer(scapy.TCP):
        tcp_layer = packet[scapy.TCP]
        flags = tcp_layer.sprintf("%TCP.flags%")
        transport_info = f"TCP {ip_layer.sport}->{ip_layer.dport} [{flags}]"
    elif packet.haslayer(scapy.UDP):
        transport_info = f"UDP {ip_layer.sport}->{ip_layer.dport}"
    elif packet.haslayer(scapy.ICMP):
        transport_info = "ICMP"
    else:
        transport_info = f"PROTO {ip_layer.proto}"

    # Standardized output for easy scanning
    print(f"[{timestamp}] {src:39} -> {dst:39} | {transport_info:25} | {len(packet)} bytes")

def main():
    parser = argparse.ArgumentParser(
        description="Bare-Bones Packet Auditor: Simple, Practical, Reliable",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-i", "--iface", help="Interface to sniff on. Default: all interfaces")
    parser.add_argument("-f", "--filter", default="", help="BPF filter, e.g. 'tcp port 443 and host 1.1.1.1'")
    parser.add_argument('--version', action='version', version=f'PacketAuditor {TOOL_VERSION}')
    args = parser.parse_args()

    print(f"--- Bare-Bones Packet Auditor v{TOOL_VERSION} ---")
    print("Philosophy: Simple, Practical, Reliable")
    if args.iface:
        print(f"Interface: {args.iface}")
    if args.filter:
        print(f"Filter: {args.filter}")
    print("Monitoring traffic... (Ctrl+C to stop)")

    try:
        # store=0 is critical to prevent memory exhaustion during long runs
        scapy.sniff(iface=args.iface, filter=args.filter, prn=audit_packet, store=0)
    except KeyboardInterrupt:
        print("\n[!] Audit stopped by user.")
        sys.exit(0)
    except PermissionError:
        print("[!] Error: Root/Admin privileges required to sniff packets.")
        print("[i] Try: sudo python3 packet_audit.py")
        sys.exit(1)
    except OSError as e:
        if "No such device" in str(e):
            print(f"[!] Error: Interface '{args.iface}' not found.")
        else:
            print(f"[!] OS Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()