# MISSILE DETECTION PROGRAM #
import time

no = int(input("How many times do i scan this area?:"))

for z in range(no):
    print("SCANNING THE AREA.....")
    time.sleep(2)

Detected = input("detcted or not?? yes/no:")

if Detected == "yes":
    print("MISSILE DETECTED LAUNCHING ANTI-MISSILE BRAMHOS*****")
    print(3)
    time.sleep(2)
    print(2)
    time.sleep(2)
    print(1)
    time.sleep(2)
    print('**Boom**')

if Detected == "no":
    print("MISSILE NOT DETECTED ... SAFE")



    
