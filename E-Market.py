class Emarket:
    def __init__(self,name):
        self.name=name
        self.items=[]
    def __getitem__(self,i):
        return self.items[i]
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return f"Emarket have {len(self)} items"
    def __repr__(self):
        return f"{self.name}:['Electronics','Groceries','Plates','Glass']"

E1=Emarket("NO NAME") # Fill any word at place of no name

E1.items.append('Electronics')
E1.items.append('Plates')
E1.items.append('Groceries')
E1.items.append('Glass')

print(E1.items)
for i in E1:
    print(i)

print(E1)
