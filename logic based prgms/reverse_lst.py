#lst = [12,13,14,15,16,17,18,20]
lst = ['Jhon','Ben','Bob','Chris','Justin','Chaitanya','Adwait']

for i in range(int(len(lst)/2)):
    rev1 = lst[i]
    rev2 = lst[(i + 1) * (-1)]

    lst[i] = rev2
    lst[(i + 1) * (-1)] = rev1

print(lst)