class Student:
    college_name="GU"
    def __init__(self,name,Id):
        self.name=name
        self.Id=Id

S1=Student("Jishan",38)
S2=Student("Gaurav",28)

print(Student.college_name)
Student.college_name='NIT'
print(S1.college_name)
print(S1.__dict__)
print(S2.college_name)