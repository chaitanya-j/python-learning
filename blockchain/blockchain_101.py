import hashlib
import block
from os import system, name

blockchain = []

def validate_blk_chain():
    pass

def add_block():
    if len(blockchain) == 0:
        print()
        print("This is a genesis block so the data is not taken from you....")
        print()
        blk_obj = block.Block('3kj13j4hbjh243b4hj23','I am a Pytonista')
        print('Block craeted with hash :',blk_obj.get_hash())
        blockchain.append(blk_obj)
        print("Total blocks :",len(blockchain))

    else:
        data = input("Please enter the Data of your choice : ")
        b_obj = block.Block(blockchain[-1].get_hash(),data)
        print('Block craeted with hash :',b_obj.get_hash())
        blockchain.append(b_obj)
        print("Total blocks :",len(blockchain))

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


while True:
    #clear()
    usr_in = input('1) Validate Block chain \n2) Add new Block \n3) Exit \n<<< ')
    if int(usr_in) == 1:
        validate_blk_chain()

    if int(usr_in) == 2:
        add_block()

    if int(usr_in) == 3:
        print("Exiting....")
        exit()