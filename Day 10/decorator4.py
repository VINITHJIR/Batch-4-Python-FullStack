def kamalesh(func):

    def saran():
        print("Before Service")
        func()
        print("After Service")

    return saran


@kamalesh #kamalesh = kamalesh(greet)
def greet():
    print("Welcome Customer")
    
greet()