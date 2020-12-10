file = open('file.txt')
f = file.readlines()

wrd_rp_d = {}
wrds_lst = []

for line in f:

    if line.endswith('\n'):
        l = line.rstrip('\n')
        ls = l.split(' ')

    else:
        ls = line.split(' ')

    
    for wrd in ls:
        wrds_lst.append(wrd)


for word in wrds_lst:
    cnt = wrds_lst.count(word)

    if cnt > 1:
        wrd_rp_d[word] = cnt
    
    else:
        continue


    