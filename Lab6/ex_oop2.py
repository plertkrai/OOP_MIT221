"""
Name: Puriwat Lertkai
ID: 111111111
Group: MIT221
"""

class Student:
    #class attributes
    uni = "RUTS"

    def __init__(self,name,id,major):
        # object attributes
        self.name = name
        self.id = id
        self.major = major

    def introduce(self):
        print(f'My name is {self.name}, '
              f'my id is {self.id} '
              f'and I am studying in {self.major} major.')


s1 = Student("Puriwat Lertkrai","111","MIT")
s1.introduce()

s2 =Student("Nattapong Keawboonma","222","AC")
s2.introduce()

s1.major = "LM"
s1.introduce()

print(s1.uni)
print(s2.uni)

Student.uni = "PSU"
print(s1.uni)
print(s2.uni)

