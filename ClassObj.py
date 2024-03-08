class Person:
    name="Jishan"
    occupation="Cyber Security Developer"
    networth=101

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
a.name="Ritik"
a.occupation="DS"

print(a.name,a.occupation)
a.info()