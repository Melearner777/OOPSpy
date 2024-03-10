class Room:
    def __init__(self, length ,bredth):
        self.lenght= length
        self.bredth= bredth

    def calculate_area(self):
        print("Area of room is", length*bredth)

length=float(input("Enter the the length of the room:"))
bredth=float(input("Enter the breadth of the room:"))

my_room=Room(length,bredth)

area=my_room.calculate_area()
print(f"Area of the room is {area} square meter") 