# A student class
class Student:
    def __init__(self,rollno,fname,lname,gender,std,div):
        self.rollno = rollno
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.std = std
        self.div = div

    def __str__(self):
        return f'Student(rollno = {self.rollno}, name = {self.fname} {self.lname}, gender = {self.gender}, class = {self.std}-{self.div})'

    def __repr__(self):
        return {'rollno':self.rollno, 'name':f'{self.fname} {self.lname}', 'gender':self.gender, 'class':f'{self.std} {self.div}'}
    
stu = Student(122,'Chaitanya','Jaipurkar','Male',7,'Dahlia')
print('calling repr: ', stu.__repr__())
print('----------------------------------------------------------------------------------------------')
print('calling str: ', stu.__str__())
print('----------------------------------------------------------------------------------------------')
class School:
    def __init__(self,sname,stype,area, city):
        self.sname = sname
        self.stype = stype
        self.area = area
        self.city = city
    
    def __str__(self):
        return f'School(name = {self.sname}, type = {self.stype}, area = {self.area}, city = {self.city})'

    def __repr__(self):
        return {'name':self.sname, 'type':self.stype, 'area':self.area, 'city':self.city}

sch = School('AVEMPS','Primary School','Erandawane','Pune')
print(sch.__repr__())
print(sch.__str__())

