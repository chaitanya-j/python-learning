from  class_person import Person

per_list = []
c = 0

while c < 5:
    name, age = input('Please enter the details [name,age]:').split(',')
    age = int(age)
    if name.upper() == 'CHAITANYA':
        chait = Person(name,age)
    else:    
        pr = Person(name,age)
        per_list.append(pr)
    c += 1
    
for p in per_list:
    #print(p)
    if p.age < chait.age:
       diff = (chait.age - p.age)
       print(f'{p.name} is younger than {chait.name} by {diff} years')

    if p.age > chait.age:
        diff2 = (p.age - chait.age)
        print(f'{p.name} is older than {chait.name} by {diff2} years')

    if p.age == chait.age:
        print(f'{p.name} and {chait.name} are of same age')


    


