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
        return f'Student(rollno = {self.rollno}, Name = {self.fname} {self.lname}, gender = {self.gender}, class = {self.std}-{self.div})'

    
class School:
    def __init__(self,sname,stype,area, city):
        self.sname = sname
        self.stype = stype
        self.area = area
        self.city = city
    
    def __repr__(self):
        return {'name':self.sname, 'type':self.stype, 'area':self.area, 'city':self.city}

sch = School('AVEMPS','Primary School','Erandawane','Pune')
print(sch.__repr__())