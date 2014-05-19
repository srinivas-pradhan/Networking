#!/usr/bin/python

import socket
from binascii import hexlify

def convert_ipv4_address():
    for ip_addr in ['127.0.0.1','192.168.1.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print 'IP Address: %s => Packed %s, Unpacked %s' \
        %(ip_addr, packed_ip_addr, hexlify(packed_ip_addr), \
          unpacked_ip_addr)

if __name__ =='__main__':
    convert_ipv4_address()