#!/usr/bin/python

import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description = 'Socket Error Examples')
    parser.add_argument('--host', action ="store", dest = "host",type = int, required=False)
    parser.add_argument('--port', action ='store', dest='port',type = int, required=False)
    parser.add_argument('--file', action="store", dest="port", type=int, required=False)
    
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args
    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print 'Error creating socket: %s' %e
        sys.exit(1)
    
    # Second try-except block - connect to given \host/port
    try:
        s.connect((host,port))
    except socket.gaierror, e:
        print 'Address related error connecting to server: %s' %e
        sys.exit(1)
    except socket.error, e:
        print 'Connection error: %s' %e
        sys.exit(1)
    
    #Third try-except block  --sending data
    try:
        s.sendall("GET %s HTTP/1.0\r\n\n\r\n" % filename)
    except socket.error, e:
        print 'Error sending data: %s' %e
        sys.exit(1)
    # Fourth block waiting on data from the remote host
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print 'Error receiving data'
            sys.exit(1)
            if not len(buf):
                break
            # write the received data
            sys.stdout.write(buf)

if __name__ =='__main__':
    main()            
    
    
    
