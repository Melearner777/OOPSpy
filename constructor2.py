class Person:

    def __init__(jishan,n,o):
        print("Hey, I am a person")
        jishan.occ=n
        jishan.name=o

    def info(jishan):
        print(f"{jishan.occ} is a {jishan.name}")

a=Person("Haris","Developer")
b=Person("DDC", "Ashoka")
c=Person(1,2)
a.info()
b.info()