#!/usr/bin/env python3

# user_input.py
import sys
import socket

if len(sys.argv) != 2:
    print("Usage: python user_input.py <position>")
    sys.exit(1)

position = int(sys.argv[1])

HOST = '127.0.0.1'
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str(position).encode())
    s.shutdown(socket.SHUT_WR)
