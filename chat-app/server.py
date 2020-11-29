# This module provides the server side code
import socket
import apputils


# Get init config parameters
id = 100
server_ip, server_port, user_creds = apputils.srv_init()

print(server_ip, server_port, user_creds)

# Create a tcp socket object
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((server_ip, server_port))
server_sock.listen(3) # 3 - max queue size
print('Server has started listening on port:', server_port)

# Important in memory data strucutures
user_objects = {}


# Listen to incoming connections from new clients
while True:
    client_sock, client_addr = server_sock.accept()
    
    login_username, login_result = apputils.srv_handle_login(client_sock, client_addr, user_creds)
    
    if login_result == True:
        print(f'Client connected {client_addr} username {login_username}')
        id += 1
        c = apputils.Client(id, client_sock, client_addr, login_username)
        print(f'Adding object for {login_username} to in-memory data structure')
        user_objects[login_username] = c
    else:
        print(f'Failed login attempt from {client_addr}, username {login_username}')