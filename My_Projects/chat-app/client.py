# This module provides the client side code
import socket
import client_utils
from os import system, name
import threading
import time

server_ip , server_port = client_utils.client_init()

print(f'Attempting to connect to the server at {server_ip}:{server_port}')

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



try:
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect((server_ip, server_port))

    logged_in = False

    
    server_msg = server_sock.recv(1024).decode('utf-8')        
    att_count = 0

    if logged_in == False:

        for _ in range(4):

            if server_msg == 'Login':
                client_utils.cl_handle_login(server_sock)
                server_msg = server_sock.recv(1024).decode('utf-8')

            elif server_msg == 'Auth Failed':
                print('Incorrect username or password. Please try again')
                client_utils.cl_handle_login(server_sock)
                server_msg = server_sock.recv(1024).decode('utf-8')

            elif server_msg == 'Welcome':
                logged_in = True
                clear()
                print('--' * 50)
                print('\t\t\tAuthentication successful!$$! Welcome to the chat app')
                print('--' * 50)
                thr = threading.Thread(target=client_utils.recv_srvr_msgs,args=[server_sock])
                th = threading.Thread(target=client_utils.handle_user_msgs,args=[server_sock])
                thr.start()
                th.start()
        
            att_count += 1
        if att_count == 3 and logged_in != True:
            print('Sorry, you have exhausted your login attempts. Aborting..')


    
            

    th.join()
    thr.join()
finally:
    server_sock.close()




