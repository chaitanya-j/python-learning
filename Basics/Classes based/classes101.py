# A student class
class Student:
    def __init__(self,rollno,fname,lname,gender,std,div,marks_dict):
        self.rollno = rollno
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.std = std
        self.div = div
        self.marks_dict = marks_dict


    def __str__(self,calc_perc):
        return f'Student(rollno = {self.rollno}, name = {self.fname} {self.lname}, gender = {self.gender}, class = {self.std}-{self.div}, perc_marks = {calc_perc(self.marks_dict)})'

    def __repr__(self,calc_perc):
        return {'rollno':self.rollno, 'name':f'{self.fname} {self.lname}', 'gender':self.gender, 'class':f'{self.std} {self.div}', 'perc_marks':calc_perc(self.marks_dict)}
    
def calc_perc(marks_dic):
        no_of_nos = len(marks_dic.values())
        base = no_of_nos * 100
        total_marks = 0
        for m in marks_dic.values():
            total_marks += m
        perc = total_marks/base * 100
        return perc

stu = Student(122,'Chaitanya','Jaipurkar','Male',7,'Dahlia', {'eng':94,'sci':90,'maths':98,'ss':80})
print('calling repr: ', stu.__repr__(calc_perc))
print('----------------------------------------------------------------------------------------------')
print('calling str: ', stu.__str__(calc_perc))
print('----------------------------------------------------------------------------------------------')


# School class
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

