# This file contains custom type definitions used by the app
# It will also provide any utility functions

import configparser
import getpass
import time




def client_init():
    '''
        This function loads the configuration data for the chat app to work.
        The configuration data is returned at the end
    '''
    config = configparser.ConfigParser()
    config.read('config.ini')

    server_ip = config.get('DEFAULT','server_ip')
    server_port = int(config.get('DEFAULT','server_port'))

    return server_ip, server_port




def cl_handle_login(server_sock):
    usrname = input('Username:')
    passwd = getpass.getpass()

    user_creds = usrname + '==' + passwd
    server_sock.send(bytes(user_creds,'utf-8'))




def handle_user_msgs(server_soc):
    while True:
        time.sleep(0.5)
        msg = input('\n\t\t\t\t\t\t\t<<< ')
        server_soc.send(bytes(msg,'utf-8'))
        
def recv_srvr_msgs(server_s):
    while True:
        dec_msg = server_s.recv(100).decode('utf-8')
        print(f'\n\t\t>>> {dec_msg}') 

        if dec_msg == 'Starting chat with':
                while True:
                    #time.sleep(0.5)
                    ms = input('<=')
                    server_s.send(bytes(ms,'utf-8'))
                    print('-------------------------------------------------------------------')
                    m = server_s.recv(1024).decode('utf-8')
                    print(m)

        if dec_msg == 'A client is chatting with you':
            print('')
            print('------------------------------ CHAT IS STARTING ------------------------------')
            print(f'\n>>> {dec_msg}')
            while True:
                rply = input('<= ')
                server_s.send(bytes(rply,'utf-8'))

        elif dec_msg == 'Sorry! The user is unavailable!':
            print(dec_msg)
