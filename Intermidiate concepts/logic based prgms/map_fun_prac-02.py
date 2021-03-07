# Calling the map function with a lambda function

# First a list of numbers to call the map function on
lst_nums = [10,20,30,40,45,60,85]

# Call the map function passing a lambda function that adds 5 to the passed number

results = list(map(lambda x: x + 5, lst_nums))
print(results)

# Equivalent normal function for the above lambda function
def add_five(num):
    return num + 5 