#Define class
class Bike:
    name=0
    gear=0
    
#create object of class
bike1=Bike()

#access attributes and assign new values
bike1.gear=11
bike1.name="Mountain Bike"

print(f"Name:{bike1.name},\nGears:{bike1.gear}")