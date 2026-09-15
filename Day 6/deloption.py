student_data = {"name" : "vinith" , "age" : 21.5 , "college" : "BIT" }

student_data.pop("name")
print(student_data)

student_data.popitem()
print(student_data)

student_data.clear()
print(student_data)

del student_data
print(student_data)