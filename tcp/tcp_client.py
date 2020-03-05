import socket
import sys
import time

client_id = sys.argv[1]
delay = sys.argv[2]
no_of_messages = sys.argv[3]
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def send(id=0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT)) 
    s.send(f"{id}".encode()) 
    s.recv(BUFFER_SIZE) 
    for i in range(int(no_of_messages)):
        s.send(f"{id}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print("Sending data:", MESSAGE)
        print("Received data:", data.decode())
        time.sleep(int(delay))
    s.close()


send(client_id)
   