from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"IP Paket: {ip_layer.src} -> {ip_layer.dst}")

sniff(prn=packet_callback, filter="ip", count=10)
