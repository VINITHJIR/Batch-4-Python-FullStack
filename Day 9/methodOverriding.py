class Payment():
    def pay(self):
        print("Payment Proceed")

class UPI(Payment):
    pass

class CARD(Payment):
    def pay(self):
            print("CARD Payment Proceed")

u1 = UPI()
u1.pay() #which class method will call

c1 = CARD()
c1.pay() #which class method will call