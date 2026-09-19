class ATM():

    def __init__(self , amount):
        self.__balance = amount
        print(f"The Rs.{amount} has been Sucessfully credited your account")


    def deposit(self , amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"The Amount has been Sucessfully Debited and Total Amount are : {self.__balance}")

    def withdrawl(self , amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount # self.__balance = self.__balance - amount
                print(f"The Rs.{amount} Amount has been Sucessfully Withdrawal and Balance Amount are : {self.__balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid number")

    def balance(self):
        print(self.__balance)

abi = ATM(100000)
abi.balance()
abi.deposit(50000)
abi.withdrawl(15000)
abi.balance()
