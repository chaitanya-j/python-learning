import hashlib
import block
from os import system, name
import time

blockchain = []

def validate_blk_chain():
    valid = False
    for n in range(len(blockchain)):
        hsh = blockchain[n].get_hash()
        if blockchain[n] == blockchain[-1]:
            print('This Blockchain is Valid!!')
            break
        prev_hsh = blockchain[n+1].prev_hash

        if hsh == prev_hsh:
            continue
            valid = True

        else:
            print('Invalid Blockchain!!')
            valid = False


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
    print("Total blocks :",len(blockchain))
    print("Applications menu :")
    print()
    usr_in = input('1) Validate Block chain \n2) Add new Block \n3) Exit \n>>> ')
    if usr_in == ' ' or usr_in == '':
        print("Please enter a valid input! Please try again")
        print("Aborting...")
        break

    if int(usr_in) == 1:
        validate_blk_chain()

    if int(usr_in) == 2:
        add_block()

    if int(usr_in) == 3:
        print("Exiting....")
        exit()
    ctr += 1