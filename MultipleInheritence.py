class Employee:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"The employee name is {self.name}")

class Reader:
    def __init__(self,book):
        self.book=book
    def show(self):
        print(f"The book is {self.book}")

class ReaderEmployee(Employee,Reader):
    def __init__(self,name,book):
        self.name=name
        self.book=book

o=ReaderEmployee("Stark","Trimidhi")
o.show() 
print(o.book)