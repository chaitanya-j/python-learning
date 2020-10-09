import csv
import utils

id_lst = []
hostname_lst = []
ip_addr_lst = []
crit_lst = []
freq_lst = []


with open('lptp_info.csv','r') as csv1:
    read = csv.reader(csv1)


    for first_char in read:

        id_lst.append(first_char[0])
        hostname_lst.append(first_char[1])
        ip_addr_lst.append(first_char[2])
        crit_lst.append(first_char[3])
        freq_lst.append(first_char[4])

    print(ip_addr_lst)