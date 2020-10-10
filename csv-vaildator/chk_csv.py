import csv
from utils import *
from models import *

id_lst = []
hostname_lst = []
ip_addr_lst = []
crit_lst = []
freq_lst = []
loc_lst = []

with open('lptp_info.csv','r') as csv1:
    reader = csv.reader(csv1)

    for row in reader:
        #print(row)
        id_lst.append(row[0])
        hostname_lst.append(row[1])
        ip_addr_lst.append(row[2])
        crit_lst.append(row[3])
        freq_lst.append(row[4])
        loc_lst.append(row[5])

print(id_lst)

# The length of any list will give the number of records in the csv file 
num_rows = len(ip_addr_lst)

# Rule objects - to collect validation results
r1 = Rule(1,'id should be integer')
r2 = Rule(2,'id should be unique')
r3 = Rule(3,'id is mandatory')

r4 = Rule(4,'hostname should be alpha-numeric')
r5 = Rule(5,'hostname should be unique')
r6 = Rule(6,'hostname is mandatory')

r7 = Rule(7,'ip-address should be valid')
r8 = Rule(8,'ip-address should be unique')
r9 = Rule(9,'ip-address is mandatory')

r10 = Rule(10,'criticality should be valid')
r11 = Rule(11,'criticality is mandatory')

r12 = Rule(12,'frequency should be integer')
r13 = Rule(13,'frequency is mandatory')

# Validate the csv fields
for i in range(1, num_rows):
    # validations on id field - r1, r2, r3
    res_id_int = chk_if_int(id_lst[i])
    res_r1 = Result(i, res_id_int, id_lst[i])
    r1.results.append(res_r1)

    res_id_unique, res_id_count = check_if_unique_in_lst(id_lst[i], id_lst)
    res_r2 = Result(i, res_id_unique, id_lst[i])
    r2.results.append(res_r2)

    res_id_mandatory = chk_if_empty(id_lst[i])
    res_r3 = Result(i, res_id_mandatory, id_lst[i])
    r3.results.append(res_r3)

# --------------------------------------------------------

    # validations on hostname field - r4, r5, r6
    res_hname_alnum = validate_hname(hostname_lst[i])
    res_r4 = Result(i,res_hname_alnum,hostname_lst[i])
    r4.results.append(res_r4)

    res_hname_unique, res_hname_count = check_if_unique_in_lst(hostname_lst[i],hostname_lst)
    res_r5 = Result(i,res_hname_unique,hostname_lst[i])
    r5.results.append(res_r5)

    res_hname_mand = chk_if_empty(hostname_lst[i])
    res_r6 = Result(i,res_hname_mand,hostname_lst[i])
    r6.results.append(res_r6)

# ----------------------------------------------------------
    
    # validations on ip-address field - r7, r8, r9
    res_ipaddr_valid = validate_ipaddr(ip_addr_lst[i])
    res_r7 = Result(i,res_ipaddr_valid,ip_addr_lst[i])
    r7.results.append(res_r7)

    res_ipaddr_unique, res_ipaddr_cnt = check_if_unique_in_lst(ip_addr_lst[i],ip_addr_lst)
    res_r8 = Result(i,res_ipaddr_unique,ip_addr_lst[i])
    r8.results.append(res_r8)

    res_ipaddr_mand = chk_if_empty(ip_addr_lst[i])
    res_r9 = Result(i,res_ipaddr_mand,ip_addr_lst[i])
    r9.results.append(res_r9)

# ---------------------------------------------------------
    
    # validations on criticality field - r10, r11
    res_crit_valid = validate_crit(crit_lst[i])
    res_r10 = Result(i,res_crit_valid,crit_lst[i])
    r10.results.append(res_r10)

    res_crit_mand = chk_if_empty(crit_lst[i])
    res_r11 = Result(i,res_crit_mand,crit_lst[i])
    r11.results.append(res_r11)

# --------------------------------------------------------

    # validations on freq field - r12, r13
    res_freq = chk_if_int(freq_lst[i])
    res_r12 = Result(i,res_freq,freq_lst[i])
    r12.results.append(res_r12)

    res_freq_mand = chk_if_empty(freq_lst[i])
    res_r13 = Result(i,res_freq_mand,freq_lst[i])
    r13.results.append(res_r13)

print('------------------------------ RESULTS -------------------------------------')

print(f'\nRule 1: {r1.name}')
for tmp_res1 in r1.results:
    if tmp_res1.res == False:
        print('\tRow#',tmp_res1.row_no, ':', tmp_res1.value)

print(f'\nRule 2: {r2.name}')
for tmp_res2 in r2.results:
    if tmp_res2.res == False:
        print('\tRow#',tmp_res2.row_no, ':', tmp_res2.value)

print(f'\nRule 3: {r3.name}')
for tmp_res3 in r3.results:
    if tmp_res3.res == False:
        print('\tRow#',tmp_res3.row_no, ':', tmp_res3.value)

print(f'\nRule 4: {r4.name}')
for tmp_res4 in r4.results:
    if tmp_res4.res == False:
        print('\tRow#',tmp_res4.row_no, ':', tmp_res4.value)

print(f'\nRule 5: {r5.name}')
for tmp_res5 in r5.results:
    if tmp_res5.res == False:
        print('\tRow#',tmp_res5.row_no, ':', tmp_res5.value)

print(f'\nRule 6: {r6.name}')
for tmp_res6 in r6.results:
    if tmp_res6.res == False:
        print('\tRow#',tmp_res6.row_no, ':', tmp_res6.value)

print(f'\nRule 7: {r7.name}')
for tmp_res7 in r7.results:
    if tmp_res7.res == False:
        print('\tRow#',tmp_res7.row_no, ':', tmp_res7.value)

print(f'\nRule 8: {r8.name}')
for tmp_res8 in r8.results:
    if tmp_res8.res == False:
        print('\tRow#',tmp_res8.row_no, ':', tmp_res8.value)

print(f'\nRule 9: {r9.name}')
for tmp_res9 in r9.results:
    if tmp_res9.res == False:
        print('\tRow#',tmp_res9.row_no, ':', tmp_res9.value)

print(f'\nRule 10: {r10.name}')
for tmp_res10 in r10.results:
    if tmp_res10.res == False:
        print('\tRow#',tmp_res10.row_no, ':', tmp_res10.value)

print(f'\nRule 11: {r11.name}')
for tmp_res11 in r11.results:
    if tmp_res11.res == False:
        print('\tRow#',tmp_res11.row_no, ':', tmp_res11.value)

print(f'\nRule 12: {r12.name}')
for tmp_res12 in r12.results:
    if tmp_res12.res == False:
        print('\tRow#',tmp_res12.row_no, ':', tmp_res12.value)

print(f'\nRule 13: {r13.name}')
for tmp_res13 in r13.results:
    if tmp_res13.res == False:
        print('\tRow#',tmp_res13.row_no, ':', tmp_res13.value)
