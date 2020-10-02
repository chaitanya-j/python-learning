stu_obj_lst = []
class Student:
    def __init__(self,fname,lname,rollno):
        self.fname = fname
        self.lname =  lname
        self.rollno = rollno

    def __str__(self):
        return f'Student(name - {self.fname}, last_name - {self.lname}, rollno - {self.rollno})'

    def __repr__(self):
        return f'rollno:{self.rollno}, first name:{self.fname}, sec name {self.lname}'
        

# creating student objects
s1 = Student('Chaitanya','Jaipurkar',343)
s2 = Student('Aditya','Kulkarni',35)
s3 = Student('Jay','Pawshe',36)
s4 = Student('Jhon','Doe',345)
s5 = Student('Chris','Chyne',3)

stu_obj_lst.append(s1)
stu_obj_lst.append(s2)
stu_obj_lst.append(s3)
stu_obj_lst.append(s4)
stu_obj_lst.append(s5)
print('Before Sort')

for stuname in stu_obj_lst:
    print('sorted :',stuname)

stu_obj_lst.sort(key=lambda x: x.rollno)

print('After sort')
for stuname in stu_obj_lst:
    print('sorted :',stuname)