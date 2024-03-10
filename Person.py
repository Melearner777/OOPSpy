from datetime import date

class Person:
    def __init__(self,name,dob,country):
        self.name=name
        self.dob=dob
        self.country=country

    def calculate_age(self):
        today=date.today()
        age=today.year- self.dob.year
        if today< date(today.year,self.dob.month , self.dob.day):
            age-=1
        return age
name=input("Enter the name:")
dob=float(input("Enter your dob:"))
county=input("Enter your country name:")
