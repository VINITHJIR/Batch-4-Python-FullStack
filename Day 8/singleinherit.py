class Employeee():
    def login(self):
        print("Login happen")

class Devloper(Employeee):
    def Access(self):
        print("Production Access Granted")

dev1 = Devloper()
dev1.login()
dev1.Access()