"""
value1 = 10
value2 = 20
value3 = 30
value4 
def sumofvalue(value1 , value2 , value3):
    print(value1 + value2 + value3)

sumofvalue( value1 , value2 , value3)
"""

value = [10 , 20 , 30 , 40]
def sumofvalue(*vini):
    print(sum(*vini))

sumofvalue(value)
sumofvalue([20, 30 , 14])