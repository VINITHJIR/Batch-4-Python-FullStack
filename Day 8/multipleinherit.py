class Camera():
    def camerafunc(self):
        print("Capture Image")

class Phone():
    def callfunc(self):
        print("Shorttime communication")

class Smartphone(Camera , Phone):
    def Property(self):
        print("Using the internet to explore the world")

s1 = Smartphone()
s1.camerafunc()
s1.callfunc()
s1.Property()