class Person:
    

    def __init__(self,name,o):
        
        self.name=name
        self.occ=o

    def info(self):
        print("Hey,I am a person")
        print(f"{self.name} is a {self.occ}")

a = Person("Jishan","Student")
b = Person("Divya","ALP")
a.info()
b.info()


