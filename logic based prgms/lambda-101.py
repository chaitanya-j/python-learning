# Examples of normal functions and their lambda equivalents

# Ex-1 - A function that returns the passed string in uppercase 
def to_upper(name):
    return name.upper()

students = ['chaitanya','tanmay','anway','raghav']
print('With normal funtion:',list(map(to_upper,students)))
print('With lambda funtion:',list(map(lambda name: name.upper(),students)))

# Ex-2 - A function that calculates percentage marks out of 500
def calc_percentage(num):
    return (num/500) * 100

scores = [345,400,390,200,490]
print('With a normal function:', list(map(calc_percentage, scores)))
print('With a lambda function:', list(map(lambda num: (num/500) * 100, scores)))


