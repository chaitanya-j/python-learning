import csv
import time 

flg = False

inp_word = input('Please enter the word:')

start = time.time()

with open('dictionary.csv','r') as csv_file:
    read_csv = csv.reader(csv_file)

    for row in read_csv:
       if row[0].lower() == inp_word.lower():
           print(f'word:{row[0]}')
           print(f'type:{row[1]}')
           print(f'meaning:{row[2]}')
           flg = True
           break

    time_taken = time.time() - start
    print('-------------------------------------------------------------------------------')
    print('Time taken to print the result :',time_taken, 'seconds')
    
    if flg == False:
        print('Word not in Dictionary!')
       
