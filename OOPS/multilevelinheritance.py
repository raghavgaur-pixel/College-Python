class Person:
    def name(self):
        print('Name...')

class Teacher(Person):
    def Qualification(self):
        print('Qualification...Ph.D must')

class HOD(Teacher):
    def experience(self):
        print('Experience...is atleast 15 years')

hod = HOD()
hod.name()
hod.Qualification()
hod.experience()    