import re

all_wrds_dict = {}
word_lst = []

def clean_line(line):
    line = line.lower()
    puncs = r"[^a-zA-Z0-9'\s]"
   
    cleaned_line = re.sub(puncs,"",line)
    return cleaned_line

with open('/home/chaitanya/Work/learning/python-learning/freq_calc/test.txt') as f:
    for line in f:
        cleaned_line = clean_line(line)
        words = cleaned_line.split()

        if isinstance(words, list):
            for word in words:
                if all_wrds_dict.get(word) == None:
                    all_wrds_dict[word] = 1
                else:
                    all_wrds_dict[word] += 1
        else:
            if all_wrds_dict.get(word) == None:
                all_wrds_dict[word] = 1
            else:
                all_wrds_dict[word] += 1




for _ in range(20):

    if (len(all_wrds_dict.keys()) > 0):
        mx = max(all_wrds_dict, key=all_wrds_dict.get)    
        print(f"{mx} : {all_wrds_dict.get(mx)}")
        del all_wrds_dict[mx]

