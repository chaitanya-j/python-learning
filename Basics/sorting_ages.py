l = []
i = 0

while i < 4:
    name,age = input("Please enter the name and age [name,age]:").split(',')
    age = int(age)
    if age <= 13:
        l.append(age)
        
    i+=1

print("--------------------------------------------------")
for z in l:
    print(z)