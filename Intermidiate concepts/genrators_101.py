def square_num(nums_list):
    for num in nums_list:
        yield (num * num)

sq_num = square_num([1,2,3,4,5,6,7,8,9,10])

print(next(sq_num)) 
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))

 