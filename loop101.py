import array as arr

arr2 = arr.array('i', [10,20,30])
print(arr2)
for i in range(len(arr2)):
    print(i)

usr = int(input("Please enter the no you want to remove:"))
o = len(arr2)
for m in range(o):
    if arr2[m] == usr:
        arr2.pop(m)
        break

print(arr2)

