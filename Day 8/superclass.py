class Animal: 
    def __init__(self, name):  
        self.name = name
        print("Animal Constructor") 

class Dog(Animal): 
    def __init__(self, name, breed):    
        super().__init__(name) # Calls Animal constructor
        self.breed = breed
        print("Dog Constructor")

d = Dog("Tommy", "Labrador") 
print(d.name) 
print(d.breed)
