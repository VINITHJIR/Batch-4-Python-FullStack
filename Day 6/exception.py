try:
    num = int(input())
    result = 100/num
    print(result)
except Exception as e:
    print(e)
finally:
    print("opertion completed")