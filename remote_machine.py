#!/usr/bin/python

import socket

def remote_machine_info():
    remotehost = 'www.python.org'
    try:
        print 'IP address %s' %socket.gethostbyname(remotehost)
    except socket.error , err_msg:
        print "%s" %(remotehost, err_msg)

if __name__ == '__main__':
    remote_machine_info()