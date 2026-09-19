def greet():
    print("Welcome Customer")

def decorator(func):

    def Wrapper():
        print("Before Service")
        func()
        print("After Service")

    return Wrapper

greet = decorator(greet)
greet()