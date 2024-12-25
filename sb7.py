import pyshark

def analyze_pcap(file_path):
    capture = pyshark.FileCapture(file_path)
    for packet in capture:
        if 'IP' in packet:
            print(f"IP: {packet.ip.src} -> {packet.ip.dst}, Protocol: {packet.highest_layer}")

# Nümunə faylı analiz edin
analyze_pcap("network_traffic.pcap")
