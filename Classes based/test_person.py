import class_person

persons = []
i = 0

while i < 1:
    name , age = input('Please enter the details [name,age]:').split(',')
    age = int(age)
    per = class_person.Person(name,age)
    persons.append(per)
    i+=1

for p in persons:
    print(p)

#per_str = Person('Pankaj',22)
#print(per_str)

#per_s = Person(name,age)
#print(per_s.__repr__())