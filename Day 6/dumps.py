import json
#convert dict to json

student_data = {"name" : "vinith" , "age" : 21.5 , "college" : "BIT" }

string = json.dumps(student_data)

print(string)
print(string[0])