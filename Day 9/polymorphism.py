class Whastapp():
    def message(self , info):
        print(f"online Message : {info}")

class Email():
    def message(self, info):
        print(f"Email Message : {info}")

class Message():
    def message(self, info):
        print(f"offline Message : {info}")

my_mail = Email()
w1 = Whastapp()
m1 = Message()


def deliver_notification(obj , data):
    obj.message(data)

deliver_notification(my_mail , "Dear Student Tommorow will be e holiday !!..")
deliver_notification(w1 , "Hi Machi nalla irukaya !!..")
deliver_notification(m1 , "Hey Bro Please call me .")