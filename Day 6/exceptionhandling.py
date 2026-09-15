try:
    num = int(input())
    result = 100/num
    print(result)
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("zero division error")


