tuple1 = ("vinithji","kishore")
print(tuple1)
templist = list(tuple1)
templist[0] = "vinithji - CTO at Bridge AI Innovation" 
templist[1] = "kishore - Founder at Bridge AI Innovation"
tuple1 = tuple(templist)
print(tuple1)