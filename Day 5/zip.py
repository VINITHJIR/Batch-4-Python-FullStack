sno = [1 , 2 , 3 , 4 , 5 , 6]
food = ["Chicken Biriyani" , "Maggi" , "Mutton Biriyani" , "Masala  Dosa" , "Waval Fish" , "Podi Idly"]
dessert  = ["browine" , "ice cream" , "kesari" , "gulab jamun" , "Rasakulla" , "Rasamalai"]

for sno ,fooditem , dessertitem in zip(sno , food , dessert):
    print(f"The S.No {sno} fooditem is {fooditem} and dessertitem is {dessertitem}")