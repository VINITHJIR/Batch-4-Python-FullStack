class studentdetails:

    def __init__(self ,name , ph , location,father):

        self.student_name = name
        self.phonenumber = ph
        self.loc = location
        self.fathername = father
        print(f"The Student name is {self.student_name} and ph is {self.phonenumber} and loc is {self.loc} and his father name is {self.fathername}")

    def calculate_marks(self, sub1 , sub2 , sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.total = sub1 + sub2 +  sub3
        print(f"the total marks are {self.total}")


student1obj = studentdetails("vinithji" , 9360385470 , "sathy" , "ramudurai")
student2obj = studentdetails("saran" , 9360385471 , "puthukottai" , "rajendran")

print(student1obj.student_name)
print(student2obj.student_name)
student1obj.calculate_marks(98 , 70 , 55)
print(student1obj.total)

student2obj.calculate_marks(980 , 700 , 550)
print(student2obj.total)
print(student1obj.total)



