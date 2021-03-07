#lst = [12,13,14,15,16,17,18,20]


lst = ['Jhon','Ben','Bob','Chris','Justin','Chaitanya','Adwait']

# Starting a for loop and passing half of the length of the list to the range function
for i in range(int(len(lst)/2)):

    # Here we are accesing the i'th position in the list
    rev1 = lst[i]

    # Here we are accesing the (i + 1) * (-1) position, which is from the opposite side of the list.
    rev2 = lst[(i + 1) * (-1)]

    # Here we are changing the values in the list 
    lst[i] = rev2
    lst[(i + 1) * (-1)] = rev1

print(lst)