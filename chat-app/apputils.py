# This file contains custom type definitions used by the app
# It will also provide any utility functions

import configparser
import csv
import getpass

class Client():
    '''
        Class to hold information for each connected client
        The server will create one object for each connected client and hold in an in-memory data structure.
    '''
    id = None
    user = None
    sock = None
    address = None

    def __init__(self, id, sock, address, user = None):
        self.id = id
        self.user = user
        self.sock = sock
        self.address = address

    def __str__(self):
        return f'Client: (id:{self.id}, user:{self.user}, address: {self.address}, sock: {self.sock})'

    def __repr__(self):
        return { 'id':self.id, 'user':self.user, 'address': self.address, 'sock': self.sock }


def srv_init():
    '''
        This function loads the configuration data for the chat app to work.
        The configuration data is returned at the end
    '''
    config = configparser.ConfigParser()
    config.read('config.ini')

    server_ip = config.get('DEFAULT','server_ip')
    server_port = int(config.get('DEFAULT','server_port'))

    user_creds = {}

    with open('creds.csv') as creds:
        creds = csv.reader(creds)
        
        for cred in creds:
            if cred[0] != 'username':
                user_creds[cred[0]] = cred[1]

    return server_ip, server_port, user_creds

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



def srv_handle_login(client_sock, client_addr, user_creds):
    '''
        This function handles the login process of the connecting client
        from the server perspective.

        Should give 3 chances for the client to clear the authentication challange

    '''
    print(f'Got a connection request from client at address {client_addr}')

    login_result = False
    login_username = None
    msg_for_client = 'Login'

    # Send the login message to the client
    client_sock.send(bytes(msg_for_client,'utf-8'))

    for _ in range(3):

        client_msg = client_sock.recv(60).decode('utf-8')
        print('Got user creds. Checking...')

        client_msg_tokens = client_msg.split('==')
        login_username = client_msg_tokens[0]

        if client_msg_tokens[1] == user_creds.get(client_msg_tokens[0]):
            login_result = True
            client_sock.send(bytes('Welcome','utf-8'))
            break
        else:
            client_sock.send(bytes('Auth Failed','utf-8'))

    return login_username, login_result

def cl_handle_login(server_sock):
    usrname = input('Username:')
    passwd = getpass.getpass()

    user_creds = usrname + '==' + passwd
    server_sock.send(bytes(user_creds,'utf-8'))


def handle_client_msgs():
    pass
