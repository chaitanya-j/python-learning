import hashlib
import block
from os import system, name
import time

blockchain = []

def validate_blk_chain():
    valid = False
    for n in range(len(blockchain) - 1):
        hsh = blockchain[n].get_hash()
        
        prev_hsh = blockchain[n+1].prev_hash

        if hsh == prev_hsh:
            valid = True
            

        else:
            valid = False

    if valid == True:
        return 'This Blockchain is Valid!!'

    else:
        return 'Invalid Blockchain!!'


def add_block():
    if len(blockchain) == 0:
        inp = input("Please enter the Data of your choice : ")
        blk_obj = block.Block('3kj13j4hbjh243b4hj23',inp)
        print('Block created with hash :',blk_obj.get_hash())
        blockchain.append(blk_obj)
        
    else:
        data = input("Please enter the Data of your choice : ")
        b_obj = block.Block(blockchain[-1].get_hash(),data)
        print('Block created with hash :',b_obj.get_hash())
        blockchain.append(b_obj)
       

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

ctr = 1
while True:
    if ctr == 1:
        print("The program may take a few seconds to start...")
    time.sleep(2)
    clear()
    print("WELCOME TO CHAITANYA'S BLOCKCHAIN DEMO!")
    print('-'*40 ,'\n')
    print("Total blocks :",len(blockchain))
    print("Applications menu :")
    print()
    usr_in = input('1) Validate block chain \n2) Add a new block \n3) Print the blockchain  \n4) Exit \n>>> ')
    if usr_in == ' ' or usr_in == '':
        print("Please enter a valid input! Please try again")
        print("Aborting...")
        break

    if int(usr_in) == 1:
        outp = validate_blk_chain()
        print(outp)

    if int(usr_in) == 2:
        add_block()

    if int(usr_in) == 4:
        print("Exiting....")
        exit()

    if int(usr_in) == 3:
        for blck in blockchain:
            print(f"Block : {blck}")
        time.sleep(5)
    ctr += 1