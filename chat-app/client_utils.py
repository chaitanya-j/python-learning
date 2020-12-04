# This file contains custom type definitions used by the app
# It will also provide any utility functions

import configparser
import getpass




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




def send_cli_msgs(server_soc):
    while True:
        msg = input('<= ')
        server_soc.send(bytes(msg,'utf-8'))
        
def recv_srvr_msgs(server_s):
    while True:
        dec_msg = server_s.recv(100).decode('utf-8')
        print(f'=> {dec_msg}') 