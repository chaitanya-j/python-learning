import statistics
import re

all_wrds_dict = {}

file = open('/home/chaitanya/Work/learning/python-learning/freq_calc/sample.txt')
#print(file.readlines())

line_list = file.readlines()


def remove_punc(line):
    if line.endswith('\n'):
        line = line.rstrip('\n')
        line = line.lower()
    puncs = "[ " " ! "  "' ( $ % &) * +  - . / : ; < = > ? @  \ ^ _ ` { , | } ~ " " ]"
    
    mod_line = re.sub(puncs," ",line)
    return mod_line.split()

mod_line_lst = []
for line in line_list:
    mod_line = remove_punc(line)
    mod_line_lst.append(mod_line)


for mod_lst_ in mod_line_lst:
    for no in range(len(mod_lst_)):
        if mod_lst_[no] in all_wrds_dict.keys():
            all_wrds_dict[mod_lst_[no]] += 1

        else:
            repetition = mod_lst_.count(mod_lst_[no])
            all_wrds_dict[mod_lst_[no]] = repetition


if len(all_wrds_dict.keys()) >= 10: 
    for itr in range(10):

        mx = max(all_wrds_dict, key=all_wrds_dict.get)    
        print(f"{mx} : {all_wrds_dict.get(mx)}")
        del all_wrds_dict[mx]

else:
    for it in range(5):

        mx = max(all_wrds_dict, key=all_wrds_dict.get)    
        print(f"{mx} : {all_wrds_dict.get(mx)}")
        del all_wrds_dict[mx]
