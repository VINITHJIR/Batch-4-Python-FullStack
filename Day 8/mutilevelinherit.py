class GrandFather():
    def gfproperty(self):
        print("500 acers")

class Father(GrandFather):
    def fproperty(self):
        print("1500 acers")

class GrandSon(Father):
    def gsproperty(self):
        print("1 Royal Enfeild Bike & iphone 18 pro max")

s1 = GrandSon()
s1.gfproperty()
s1.fproperty()
s1.gsproperty()