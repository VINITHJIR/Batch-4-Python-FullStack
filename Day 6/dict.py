student_data = {"name" : "vinith" , "age" : 21.5 , "college" : "BIT" }
print(student_data)

#access

print(student_data["college"])

student_data["college"] = "Karpagam deemed university"
print(student_data)

student_data["fullname"] = student_data["name"]

del student_data["name"]
print(student_data)