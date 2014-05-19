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
    filename = given_args.file
    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print 'Error creating socket: %s' %e
        sys.exit(1)
    
    # Second try-except block - connect to given host/port
    try:
        s.connect((host,port))
        
    
    
