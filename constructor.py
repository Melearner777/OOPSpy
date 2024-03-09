class Person:
    

    def __init__(self,name,o):
        print("Hey,I am a person") #This will everytime print if object will created.
        self.name=name
        self.occ=o

    def info(self):
        
        print(f"{self.name} is a {self.occ}")

a = Person("Jishan","Student")
b = Person("Divya","ALP")
a.info()
b.info()
b.info()


