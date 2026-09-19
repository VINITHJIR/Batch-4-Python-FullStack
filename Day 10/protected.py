class FatherShopCbe():
    def __init__(self , value):
        self._weightofrice = value
        print(self._weightofrice)

    def result(self):
        print(self._weightofrice)


class SonShopErode(FatherShopCbe):

   def __init__(self , value):
       super().__init__(value)
       print("changed")

s1 = SonShopErode(78)
s1.result()

