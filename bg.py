# student_data={'name':'Riya','marks':[98,97,65,87]}
# def avg_marks(student_data):
    # return sum(student_data['marks'])/len(student_data['marks'])
# print(avg_marks(student_data))

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg_marks(self):
        return sum(self.marks)/len(self.marks)
    
S1=Student("Jishan",[88,96,69,81])
S2=Student("Gaurav",[65,98,87,59])
print(S1.avg_marks())
print(Student.avg_marks(S1))
print(S2.avg_marks())