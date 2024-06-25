# Constructor Use
class Employee:
    def __init__(self, name, age, salary, post):
        self.name = name
        self.age = age
        self.salary = salary
        self.post = post

    def PrintDetails(self):
        print("Employee Name is", self.name, "\nAge is", self.age,
              "\nsalary is", self.salary, "\nAnd Post is", self.post)


empName = input("Enter Emp. Name -> ")
empAge = input("Enter Emp. Age -> ")
empSalary = input("Enter Emp. Salary -> ")
empPost = input("Enter Emp. Post -> ")
emp1 = Employee(empName, empAge, empSalary, empPost)
print(emp1.PrintDetails())
