import csv
import getpass
import configparser

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

# -------------------------------------------------------------------------------------------------------------------------- #

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

# -------------------------------------------------------------------------------------------------------------------------- #

def handle_client_msgs(client_obj, client_dict):
    while True:
        msg = client_obj.sock.recv(1024).decode('utf-8')
        print(msg)
        if msg.upper().startswith('START CHAT'):
            spl_msg = msg.split(' ')
            obj = client_dict.get(spl_msg[2]) 
            print(f'$$$ Attempt to start chat with user {obj}')
            if obj != None:
                client_obj.sock.send(bytes(f'Starting chat with {spl_msg[2]}....','utf-8'))

                obj.sock.send(bytes('A client is chatting with you','utf-8'))
                while True:
                    cli2_recv = obj.sock.recv(1024).decode('utf-8')
                    client_obj.sock.send(bytes(f'[{obj.user}] {cli2_recv}','utf-8'))


                while True:
                    cl_msg = client_obj.sock.recv(1024).decode('utf-8')
                    print(cl_msg)
                    obj.sock.send(bytes(f'[{client_obj.user}] : {cl_msg}','utf-8'))


            else:
                client_obj.sock.send(bytes('Sorry! The user is unavailable!','utf-8'))
        
        else:
            ack = f'You just sent me : {msg}'
            print(ack)
            client_obj.sock.send(bytes(ack,'utf-8'))

# -------------------------------------------------------------------------------------------------------------------------- #

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
