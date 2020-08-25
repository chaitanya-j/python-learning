no = int(input("enter the number:"))

print("Trying to find the approximate square root... hold on.. i may take some time")

flag = False

#lst = [i/1000 for i in range(no * 1000)]

#print(len(lst), lst[0], lst[-1])

sq = 0.0
sqroot = 0.0
cnt = 0

for i in range(no):
    cnt = cnt + 1
    sq = i * i

    #print("i = ", i, " sq = ", sq)

    if sq == no:
        print("Found the perfect square root. It is ", i)
        flag = True
        break
    
    elif sq > no:
        break
    
    sqroot = i    


if flag == False:

    print("Sorry. Could not find the perfect square root. But I have reached this number which is pretty close ", sqroot)    
    print("I have checked ", cnt, " numbers so far... ")
    print("Let me exert a bit more.. I will increment by 1/1000th from now onwards to reach a near perfect result")
    print("Value of sqroot = ", sqroot)

    decimal_lst = [ sqroot + (j/100000) for j in range(10000) ]
    decimal_lst.
    #decimal_lst = [ j/1000 for j in range(sqroot, (sqroot+1)*1000) ]
    
    print(len(decimal_lst), decimal_lst[0], decimal_lst[-1])

    for k in decimal_lst:
        cnt = cnt + 1
        sq = k * k

        #print("i = ", i, " sq = ", sq)

        if sq > no:
            flag = True
            break
    
        sqroot = k
 
print("Near perfect square root of your number is ", sqroot)
print("Total numbers checked finally = ", cnt)
