import json
#convert dict to json

student_data = {"name" : "vinith" , "age" : 21.5 , "college" : "BIT" }

stringdata = json.dumps(student_data)
print(stringdata, "stringdata")
print(stringdata[0])
#convert json to dictionary

dictdata = json.loads(stringdata)

print(dictdata , "dictdata")
print(dictdata["name"])
