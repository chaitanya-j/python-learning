# Importing the required modules
import csv
from utils import *
from models import *

# Creating empty lists to store the respective values from the csv in their respective lists:
# Creating lists is very important for uniqeness check!
# We are using lists and not any other data type because 'a list is always in order'
id_lst = []
hostname_lst = []
ip_addr_lst = []
crit_lst = []
freq_lst = []
loc_lst = []
header_lst = []

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

r14 = Rule(14,'header should be exactly the same as required')


# Opening and readig the CSV file using reader method in read mode
# Note : Reader object returns list of lists each sublist will contain a row from the CSV
with open('lptp_info.csv','r') as csv1:
    reader = csv.reader(csv1)
    ctr = 0

    # Using a for loop to access the sublists from reader object
    for row in reader:
        
        # If the counter is '0' then we will append the whole row of headers into the list 'header_lst'
        if ctr == 0:
            header_lst = list(row)

            # validation for header field - r14
            # validation : the headers should be exactly the same as - 'id,hostname,ip-address,criticality,freq,location'
            res_headers_valid = chk_headers_v2(header_lst)
            res_r14 = Result(1,res_headers_valid,header_lst)
            r14.results.append(res_r14)
            ctr += 1

        # Appending the values of each sublist into their respective lists
        id_lst.append(row[0])
        hostname_lst.append(row[1])
        ip_addr_lst.append(row[2])
        crit_lst.append(row[3])
        freq_lst.append(row[4])
        loc_lst.append(row[5])

# The length of any list will give the number of records in the CSV file 
num_rows = len(ip_addr_lst)


# Validate the CSV fields
for i in range(1, num_rows):

    # THE FOLLOWING LOGIG IS APPLICABLE TO ALL THE VALIDATIONS BELOW :
    # LOGIC : Appliying the respective functions according to the 'rules'
    #       : Then creating a result object and storing the "rollno", "value", and the "result" that came from appliying the function
    #       : Then we are appending the created result object in the respective rule object's results list

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
    res_freq_valid = chk_if_int(freq_lst[i])
    res_r12 = Result(i,res_freq_valid,freq_lst[i])
    r12.results.append(res_r12)

    res_freq_mand = chk_if_empty(freq_lst[i])
    res_r13 = Result(i,res_freq_mand,freq_lst[i])
    r13.results.append(res_r13)

    


print('------------------------------ RESULTS -------------------------------------')

# Printing the results that came from checking each rule object's results list's objects's result
res_lst1 = chk_res_lst(r1.results)
if res_lst1 == True:
    print(f'Rule 1: {r1.name} [OK]')
else:
    print(f'Rule 1: {r1.name} [NOT OK]')
for tmp_res1 in r1.results:
    if tmp_res1.res == False:
        print('\tRow#',tmp_res1.row_no, ':', tmp_res1.value)

  
res_lst2 = chk_res_lst(r2.results)
if res_lst2 == True:
    print(f'Rule 2: {r2.name} [OK]')
else:
    print(f'Rule 2: {r2.name} [NOT OK]')
for tmp_res2 in r2.results:
    if tmp_res2.res == False:
        print('\tRow#',tmp_res2.row_no, ':', tmp_res2.value)

    
res_lst3 = chk_res_lst(r3.results)
if res_lst3 == True:
    print(f'Rule 3: {r3.name} [OK]')
else:
    print(f'Rule 3: {r3.name} [NOT OK]')
for tmp_res3 in r3.results:
    if tmp_res3.res == False:
        print('\tRow#',tmp_res3.row_no, ':', tmp_res3.value)

    
res_lst4 = chk_res_lst(r4.results)
if res_lst4 == True:
    print(f'Rule 4: {r4.name} [OK]')
else:
    print(f'Rule 4: {r4.name} [NOT OK]')
for tmp_res4 in r4.results:
    if tmp_res4.res == False:
        print('\tRow#',tmp_res4.row_no, ':', tmp_res4.value)

    
res_lst5 = chk_res_lst(r5.results)
if res_lst5 == True:
    print(f'Rule 5: {r5.name} [OK]')
else:
    print(f'Rule 5: {r5.name} [NOT OK]')
for tmp_res5 in r5.results:
    if tmp_res5.res == False:
        print('\tRow#',tmp_res5.row_no, ':', tmp_res5.value)

    
res_lst6 = chk_res_lst(r6.results)
if res_lst6 == True:
    print(f'Rule 6: {r6.name} [OK]')
else:
    print(f'Rule 6: {r6.name} [NOT OK]')
for tmp_res6 in r6.results:
    if tmp_res6.res == False:
        print('\tRow#',tmp_res6.row_no, ':', tmp_res6.value)



res_lst7 = chk_res_lst(r7.results)
if res_lst7 == True:
    print(f'Rule 7: {r7.name} [OK]')
else:
    print(f'Rule 7: {r7.name} [NOT OK]')
for tmp_res7 in r7.results:
    if tmp_res7.res == False:
        print('\tRow#',tmp_res7.row_no, ':', tmp_res7.value)

    
res_lst8 = chk_res_lst(r8.results)
if res_lst8 == True:
    print(f'Rule 8: {r8.name} [OK]')
else:
    print(f'Rule 8: {r8.name} [NOT OK]')
for tmp_res8 in r8.results:
    if tmp_res8.res == False:
        print('\tRow#',tmp_res8.row_no, ':', tmp_res8.value)


res_lst9 = chk_res_lst(r9.results)
if res_lst9 == True:
    print(f'Rule 9: {r9.name} [OK]')
else:
    print(f'Rule 9: {r9.name} [NOT OK]')
for tmp_res9 in r9.results:
    if tmp_res9.res == False:
        print('\tRow#',tmp_res9.row_no, ':', tmp_res9.value)
                
                

res_lst10 = chk_res_lst(r10.results)
if res_lst10 == True:
    print(f'Rule 10: {r10.name} [OK]')
else:
    print(f'Rule 10: {r10.name} [NOT OK]')
for tmp_res10 in r10.results:
    if tmp_res10.res == False:
        print('\tRow#',tmp_res10.row_no, ':', tmp_res10.value)

    
res_lst11 = chk_res_lst(r11.results)
if res_lst11 == True:
    print(f'Rule 11: {r11.name} [OK]')
else:
    print(f'Rule 11: {r11.name} [NOT OK]')
for tmp_res11 in r11.results:
    if tmp_res11.res == False:
        print('\tRow#',tmp_res11.row_no, ':', tmp_res11.value)


res_lst12 = chk_res_lst(r12.results)
if res_lst12 == True:
    print(f'Rule 12: {r12.name} [OK]')
else:
    print(f'Rule 12: {r12.name} [NOT OK]')
for tmp_res12 in r12.results:
    if tmp_res12.res == False:
        print('\tRow#',tmp_res12.row_no, ':', tmp_res12.value)


res_lst13 = chk_res_lst(r13.results)
if res_lst13 == True:
    print(f'Rule 13: {r13.name} [OK]')
else:
    print(f'Rule 13: {r13.name} [NOT OK]')
for tmp_res13 in r13.results:
    if tmp_res13.res == False:
        print('\tRow#',tmp_res13.row_no, ':', tmp_res13.value)


res_lst14 = chk_res_lst(r14.results)
if res_lst14 == True:
    print(f'Rule 14: {r14.name} [OK]')
else:
    sep = ','
    print(f'Rule 14: {r14.name} [NOT OK]')
    print('\tExpected header:', 'id,hostname,ip-address,criticality,freq,location')
    print('\tReceived header:',sep.join(r14.results[0].value))
    


    
