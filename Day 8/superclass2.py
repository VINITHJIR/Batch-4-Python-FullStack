class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()      # Calls parent methodprint("Dog barks")

d = Dog() 
d.sound()
