class Employee():
    def get_salary(self):
        print("Received Salary")

class Devloper(Employee):
    def write_code(self):
        print("Found Innovation")

class Tester(Employee):
    def Testing(self):
        print("Find Issue")

class Finance(Employee):
    def Calculate_salary(self):
        print("Make Calculate")

dev1 = Devloper()
dev1.get_salary()
dev1.write_code()
T1 = Tester()
T1.get_salary()
T1.Testing()