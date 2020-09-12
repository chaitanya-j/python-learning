# This program demonstrates the basics of exception handling
# Exception handling: Catching run-time errors and not letting the program crash due to them
# Examples: Devide by zero error, unexpected input 'ValueError' etc

# Let us see how to handle the ValueError which is thrown by functions like int(), float() etc.
# When you pass a string that does not contain a number, these functions throw the ValueError



usr_nums = []

# Let us put the call to the int() function inside a try block
while True:
    # Accept the user input
    usr_input = input('Enter a number: ')

    # Now the variable usr_input can contain anything - a number or something else
    # If it is anything else than a number, we will get ValueError from the int() call
    try:
        usr_input_int = int(usr_input)
        usr_nums.append(usr_input_int)

        print(f'You entered {usr_input_int}')
    except ValueError:
        print('Sorry boss, you need to enter a number!!')

    ch = input('Do you want to enter another number(Y/N)? : ')
    if ch == 'Y' or ch == 'y':
        continue
    else:
        break

print(f'Your entered numbers {usr_nums}')
print('Thank you for using my program')
