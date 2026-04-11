class Student:
    def name(self):
        print('Name...')

class Academic_Performance(Student):
    def Acad_score(self):
        print("Acaademic Score...90% and above")

class ECA(Student):
    def ECA_score(self):
        print("ECA Score...60% and above")

class Result(Academic_Performance, ECA):
    def Eligibility(self):
        print("Minimum Eligibility to Apply")
        self.Acad_score()
        self.ECA_score()

R = Result()
R.Eligibility()