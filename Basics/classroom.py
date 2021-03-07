studentMarks = {}
students = {}
n = int(input('How many students do you want?: '))
for rollno in range(1, n+1):
    stname = input('Enter name of the student: ')
    stmarks = int(input(f'Enter the marks for {stname}: '))
    students[rollno] = stname
    studentMarks[rollno] = stmarks


print('Final classroom is: ',students,studentMarks)
