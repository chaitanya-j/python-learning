try:
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect((server_ip, server_port))

    logged_in = False

    if logged_in == False:
while True:
    server_msg = server_sock.recv(1024).decode('utf-8')        
    att_count = 0

    for _ in range(4):
        
       
        if server_msg == 'Login':
            apputils.cl_handle_login(server_sock)
        
        elif server_msg == 'Auth Failed':
            print('Incorrect username or password. Please try again')
            apputils.cl_handle_login(server_sock)
            
        elif server_msg == 'Welcome':
            logged_in = True
            clear()
            print('--' * 50)
            print('\t\t\tAuthentication successful! Welcome to the chat app')
            print('--' * 50)
            
        server_msg = server_sock.recv(1024).decode('utf-8')
        att_count += 1
        if att_count == 3 and logged_in != True:
            print('Sorry, you have exhausted your login attempts. Aborting..')

        if server_msg.upper().startswith('STARTING CHAT WITH'):
        msg = input('<= ')
        server_sock.send(bytes(msg,'utf-8'))
        

    else:
        print('Now waiting for server messages or your activity')


finally:
    server_sock.close()









def send_cli_msgs(server_soc):
    while True:
        msg = input('<= ')
        server_soc.send(bytes(msg,'utf-8'))
        
def recv_srvr_msgs(server_s):
    dec_msg = server_s.recv(1024).decode('utf-8')
    print(f'=> {dec_msg}') 




