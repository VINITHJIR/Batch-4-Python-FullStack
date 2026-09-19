def greet():
    print("Welcome Customer")

def Kamalesh(vinithanna):

    def saran():
        print("Before Service")
        vinithanna()
        print("After Service")

    return saran

abi = Kamalesh(greet)
abi()