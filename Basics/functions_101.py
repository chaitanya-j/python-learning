def say_hello(n):

    # Saying hello to the user.
    print(f"Hello {n}")
    
def do_magic(foo):

    # Checking if foo is callable. Call only if it is a function
    if callable(foo):
        print("I recived", foo)
        foo("Chaitanya")
    
    # If foo is not callable, it will do the following.
    else:
        print("Please give a function")

        
print("Starting....")
do_magic(say_hello)
