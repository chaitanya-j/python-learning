import threading
import time

def do_sleep(t):
    sleep_time = t * 4
    print(f'Thread-{t}: Needs to sleep for {sleep_time} seconds')
       
    for _ in range(1,sleep_time):
        print(f'Thread-{t}: {sleep_time} seconds remaining')
        time.sleep(1)
        sleep_time -= 1
    
    print(f'Thread-{t} completed')
        
print('Starting the thread demo..')
threads = []

for i in range(1,6):
    #print('i = ', i)
    th_tmp = threading.Thread(target=do_sleep, args=[i])
    th_tmp.start()
    threads.append(th_tmp)    

for th in threads:
    th.join()

print('Program completed')