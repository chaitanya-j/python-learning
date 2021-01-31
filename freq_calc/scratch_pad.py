b = {'name':'chaitanya',
     'rollno':45,
     'div':'dahlia'}
a = {'name':'neel',
     'rollno':34}

keys = b.keys()

for i in keys:
    val = a.get(i)
    print(val,i)
    txt = "This table {tablename} is not found".format(tablename = i)
    print(txt)