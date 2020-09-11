import array as arr
print("Please enter numbers greater than 0")
arr2 = arr.array('i', [])

x = int(input("How many numbers do you want to add in the array?:"))
if x > 0:
    for e in range(x):
        no = int(input("Please enter the no:"))
        arr2.append(no)

    print(arr2)

    i = input("Do you want to remove any value from the array?:")
    if i == "yes":
        r = int(input("Please enter the place no of the value in the list which you want to remove:"))
        arr2.pop(r)

    print(arr2)

    if i == "no":
        exit()

else:
    print("Please enter a no greater than 0, please try again")