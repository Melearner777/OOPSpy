class Rectangle:
    def __init__(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth

    def Area(self):
        return self.length*self.breadth
    

length1=float(input("Enter the length of the first rectangle:"))
breadth1=float(input("Enter the breadth of the first rectangle:"))

length2=float(input("Enter the length of the second rectangle:"))
breadth2=float(input("Enter the breadth of the second rectangle:"))

Rectangle1= Rectangle(length1,breadth1)
Rectaangle2=Rectangle(length2,breadth2)

print(f"Area of the first rectangle:{Rectangle1.Area()}")
print(f"Area of the second rectangle:{Rectaangle2.Area()}")