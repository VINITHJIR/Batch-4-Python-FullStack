class A():
    def show(self):
        print("class A")

class B(A):
   pass

class C(A):
    def show(self):
        print("class C")

class D(B , C):
    pass

obj = D()
obj.show()