#to print only value of dictionary not key so modification in client print
# Scapy is the library used for network scanning 
import scapy.all as scapy


def scan(ip):
    # IP is the IP range to be scanned
    # Below line creates an ARP packet
    arp_request = scapy.ARP(pdst=ip)

    # ff:ff:ff:ff:ff:ff as destination mac means broadcast
    # This line creates an ether message
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # This line combines ether packet and ARP packet
    arp_request_broadcast = broadcast/arp_request

    # This sends our created packet in the network
    # Timeout is the time our scanner waits for the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # It will only return me answered list by writing index [0]
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "Mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(results_list):
    print("IP \t\t\t\t MAC Address\n")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["Mac"])
        
#scan("192.168.254.2")
scan_result = scan("192.168.1.0/24")
print_result(scan_result)
