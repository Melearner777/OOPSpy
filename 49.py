class Library:
    def __init__(self): #Dender method used for getting subject to add accordingly
        self.subjects=[]

    def __len__(self): #Dender method use for getting subject by there number on list
        return len(self.subjects)
    
    def __getitem__(self,i): #Dender method used for getting subject name
        return self.subjects[i]
    
b1=Library()

b1.subjects.append('Python')
b1.subjects.append('Jishan')
b1.subjects.append('C++')

print(len(b1))
print(Library.__getitem__(b1,0))

for i in b1: #This is used to print all subject List
    print(i)