class Vector():
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i +{self.j}j +{self.k}k"
    
    def __add__(self,other_vector):
        return Vector(self.i+other_vector.i,self.j+other_vector.j,self.k+other_vector.k)
    
v1= Vector(3,5,6)
print(v1)
v2=Vector(5,6,7)
print(v2)

print(v1+v2)