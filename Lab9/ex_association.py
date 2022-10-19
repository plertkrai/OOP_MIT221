"""
Name: Puriwat Lertkai
ID: 111111111
Group: MIT221
"""

# Class Relations - Association

class Student:
    #class attribute
    lst_teacher = list()
    def __init__(self,name,major,project):
        self.name = name
        self.major = major
        self.project = project
    def student_info(self):
        print(f'STD Name: {self.name} Major: {self.major}')
        print(f'Working on project: {self.project}')
        print(f'Advisor list: ')
        if len(self.lst_teacher) ==0:
            print("\tNo advisor.")
        else:
            for x in self.lst_teacher:
                x.teacher_info()
    def add_advisor(self,Teacher):
        self.lst_teacher.append(Teacher)

class Teacher:
    lst_student = list()

    def __init__(self,name):
        self.name = name

    def teacher_info(self):
        print(f'Teacher name: {self.name}')

    def add_advisee(self,Student):
        self.lst_student.append(Student)

    def advisee_info(self):
        if len(self.lst_student) ==0:
            print("Have no student.")
        else:
            for x in self.lst_student:
                print(x.name,x.project)

s1 = Student("John","MIT","IoT")
s2 = Student("Boy","MIT","NLP")

t1 = Teacher("Puriwat")
t2 = Teacher("Phornprasert")

#s1.student_info()
s1.add_advisor(t1)
s1.add_advisor(t2)

s1.student_info()

t1.add_advisee(s1)
t1.add_advisee(s2)

t1.teacher_info()
t1.advisee_info()
