from abc import ABC, abstractmethod

class Payment(ABC):
      @abstractmethod
      def pay(self):
             pass

class UPIPayment(Payment):
        def pay(self):
            print("Processing UPI Payment")

class CardPayment(Payment):
       def pay(self):
           print("Processing Card Payment")


upi = UPIPayment()
card = CardPayment()
upi.pay()
card.pay()
