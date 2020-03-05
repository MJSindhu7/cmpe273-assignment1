import socket
import _thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
    
def new_client(conn,addr):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: 
            #print('No data received.')
            break
        #client_data = data.decode()
        #client_data_split = client_data.split(':')
        print(f"Received data:{data.decode()}")
        conn.send("pong".encode())

    #conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server started at port {}.".format(TCP_PORT))
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

while True:
    c,addr = s.accept()
    data = c.recv(BUFFER_SIZE)
    client_data = data.decode()
    client_data_split = client_data.split(':')
    c.send("ok".encode())
    print("Connected Client:{}.".format(client_data_split[0]))
    _thread.start_new_thread(new_client,(c,addr))

s.close()