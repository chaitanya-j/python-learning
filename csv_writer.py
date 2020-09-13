from csv import DictWriter

# my list of dicts
dicts = []

d1 = {'rollno': 100, 'name':'Chaitanya Jaipurkar'}
d2 = {'rollno': 101, 'name':'Vishrut Vaishampayan'}
d3 = {'rollno': 102, 'name':'Neel Deshmukh'}
d4 = {'rollno': 103, 'name':'Samarth Joshi'}

dicts.append(d1)
dicts.append(d2)
dicts.append(d3)
dicts.append(d4)

print(dicts)

# Attempting to write a csv file
with open('students.csv','w') as csv_out:
    csv_writer = DictWriter(csv_out, d1.keys())
    csv_writer.writeheader()
    csv_writer.writerows(dicts)

print('CSV file has been written by name students.csv. Pls check')
    