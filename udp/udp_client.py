import socket
from func_timeout import func_timeout
import random


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"
wait_time = 3

def connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def send(id=0):
    try:
        s = connection()
        print("Connected to the server.")
        client_ack = 0
        print("Starting a file (upload.txt) upload...")
        with open('upload.txt', 'r') as file:
            msg = file.readline()
            msg_st = [msg,5]
            while msg:
                rand = random.randint(1,100000)
                if msg != msg_st[0]:
                    msg_st = [msg,5]
                #Sending a random number for each package along with message
                #print("{}".format(msg))
                s.sendto(f"{rand}:{client_ack}:{msg}".encode(),(UDP_IP, UDP_PORT))
                try:
                    data, ip = func_timeout(wait_time, s.recvfrom,(BUFFER_SIZE,))
                    data_rcvd = data.decode()
                    print("Received ack({}) from the server.".format(data_rcvd.strip()))
                    data_split = data_rcvd.split(':')
                    if(client_ack+1 != int(data_split[0])):
                        raise timeout
                    else:
                        msg = file.readline()
                        client_ack = int(data_split[0]) + 1
                except:
                    print("Didn't receive acknowledgement retrying")
                    msg_st[1] -=1
                    if msg_st[1]>0:
                        s = connection()
                    else:
                        exit()
        s.sendto("".encode(),(UDP_IP, UDP_PORT))            
        print("File upload successfully completed.")
    except socket.error:
        print("Error -->",socket.error)
        exit()

send()