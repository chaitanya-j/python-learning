num = 10
nums_lst = []

for n in range(10):
    nums_lst.append(num)
    num -= 1
    
print(nums_lst)

mult = 1
for calc in nums_lst:
    mult = calc * mult

print(mult)