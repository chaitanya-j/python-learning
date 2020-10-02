# Lets say, we have some list as below 
# It could be a list of just anything - strings, numbers or other class objects
children = ['Chaitanya','Tanmay','Raghav','Mrunmayee','Anvay','Adwait']

# Now we want to do something with each member of the list - say we want to greet each child with a 'Hello'
# Lets define a say_hello function that takes in a child's name and then returns a greeting for that child
def say_hello(name):
    return f'Hi {name}!'

# Traditional way of doing this - using a for loop
for child in children:
    greeting = say_hello(child)
    print(greeting)

# New way of doing it - using the python map function
greets = map(say_hello,children)

print(list(greets))

# Lets define another function - say which converts the name to UPPERCASE
def to_upper(name):
    return name.upper()

uppers = list(map(to_upper,children))
print(uppers)