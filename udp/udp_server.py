import socket
import json

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
collection = {}

def listen_forever():
    print("Server started at port  {}.".format(UDP_PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print("Accepting a file upload...")
    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        # reply back to the client
        if not data: 
            print("Upload successfully completed.")
            with open('server_collected_upload.txt', 'w') as file:
                for key, value in collection.items():
                    file.write('%s:%s\n' % (key, value.rstrip("\n")))
            file.close()
            continue
        ser_data = data.decode()
        srv_split_data = ser_data.split(":")
        ack_return = int(srv_split_data[1]) + 1
        #print("Hiii---{}".format(str(srv_split_data[3])))
        collection.update({int(srv_split_data[2]) : str(srv_split_data[3])})
        #print(collection)
        MESSAGE = str(ack_return)+":"+str(srv_split_data[3]) 
        s.sendto(MESSAGE.encode(), ip)
    
    
listen_forever()