import hashlib
import block
from os import system, name
import time

blockchain = []

def validate_blk_chain():
    valid = False
    for n in range(len(blockchain) - 1):
        curr_blk_hsh = blockchain[n].get_hash()
        
        nxt_blk_prev_hsh = blockchain[n+1].prev_hash

        if curr_blk_hsh == nxt_blk_prev_hsh:
            valid = True
            

        else:
            valid = False
            print(f"Hash of the current block : {blockchain[n].get_hash()}")
            print(f"Previous hash of next block : {blockchain[n+1].prev_hash}")
            return 'Invalid Blockchain!!'


    if valid == True:
        return 'This Blockchain is Valid!!'


def add_block():
    if len(blockchain) == 0:
        inp = input("Please enter the Data of your choice : ")
        blk_obj = block.Block('3kj13j4hbjh243b4hj23',inp)
        print('Block created with hash :',blk_obj.get_hash())
        blockchain.append(blk_obj)
        
    else:
        data = input("Please enter the Data of your choice : ")
        b_obj = block.Block(blockchain[-1].get_hash(), data)
        print('Block created with hash :',b_obj.get_hash())
        blockchain.append(b_obj)

def tamper_block():
    inp = int(input("Block no : "))     
    if blockchain[inp-1] in blockchain:
        tamp_block = blockchain[inp-1] 
        print(f"Previous data : {tamp_block.data}")
        data2 = input("Changed data : ")
        tamp_block.data = data2
        print(f"Data after change : {tamp_block.data}")

    else:
        print("Block not in blockchain!")



def clear():
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

starting = True
while True:
    if starting == True:
        print("The program may take a few seconds to start...")
        starting = False

    time.sleep(2)
    clear()
    print("WELCOME TO CHAITANYA'S BLOCKCHAIN DEMO!")
    print('-'*40 ,'\n')
    print("Total blocks :",len(blockchain))
    print("Applications menu :")
    print()
    usr_in = input('1) Add a new block \n2) Print the blockchain \n3) Validate block chain \n4) Change block data \n5) Exit \n>>> ')
    if usr_in == ' ' or usr_in == '':
        print("Please enter a valid input! Please try again")
        


    elif int(usr_in) == 3:
        outp = validate_blk_chain()
        print(outp)

    elif int(usr_in) == 1:
        add_block()

    elif int(usr_in) == 5:
        print("Exiting....")
        exit()

    elif int(usr_in) == 2:
        for blck in blockchain:
            print(blck)
        time.sleep(5)

    elif int(usr_in) == 4:
        tamper_block()
        time.sleep(5)