# Mac address changer
import argparse
import subprocess as sub

# parser = argparse.ArgumentParser(description='A')
# parser.add_argument('indir', type=str, help='Input for videos')
# parser.add_argument('outdir', type=str, help='Output for videos')
# args = parser.parse_args()
# print(args.indir)

'''
parser = argparse.ArgumentParser(description='A')
parser.add_argument('-rdc',dest='tp')
options = parser.parse_args()
tp = options.tp
print(tp, tp, tp)
'''
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='Interface name whose MAC is to be changed')
    parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC Address')
    options = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify an interface in the arguments, use --help for more info.')
    elif not options.new_mac:
        parser.error('[-] Please specify a new MAC Address, use --help for more info.')
    return options


def change_mac(interface, new_mac):
    if len(new_mac) != 17:
        print('[-] Please enter a valid MAC Address')
        quit()

    print('\n[+] Changing MAC for interface '+interface+' to '+ new_mac)
    sub.call(['sudo', 'ifconfig', interface, 'down'])
    sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    sub.call(['sudo', 'ifconfig', interface, 'up'])

    
command_args = get_args()
change_mac(command_args.interface, command_args.new_mac)
