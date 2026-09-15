def returnfunc():
    return [1 , 2 , 3 , 4 , 5]

print(returnfunc())


#yield

def yieldfunc():
   yield 1
   yield 2
   yield 3

print(next(yieldfunc()))