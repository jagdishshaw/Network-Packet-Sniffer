from scapy.all import sniff

def packet_callback(packet):
    # This function is triggered for every packet captured
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        print(f"Packet: {ip_src} -> {ip_dst}")

# Start the sniffer
# filter="ip" ensures we only capture standard IP traffic
print("Sniffing started... (Press Ctrl+C to stop)")
sniff(filter="ip", prn=packet_callback, store=0)