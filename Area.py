class Room:
    length=0.0
    breadth=0.0
    # method to calculate the area
    def calculate_area(self):
        print("Area of room is:" ,self.length*self.breadth)
    
#create object of the room
study_room=Room()

#assign values of the attributes
study_room.length=42.4
study_room.breadth=30.8
#acess the method inside the class
study_room.calculate_area()