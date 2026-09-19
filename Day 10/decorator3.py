def decorator(func):

    def Wrapper():
        print("Before Service")
        func()
        print("After Service")

    return Wrapper


@decorator #greet = decorator(greet)
def greet():
    print("Welcome Customer")
    
greet()