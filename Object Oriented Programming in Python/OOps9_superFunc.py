class person():
    def __init__(self, fname, lastname):
        self.firstname = fname
        self.lastname = lastname

    def display(self):
        print(self.firstname, self.lastname)


class student(person):
    def __init__(self, fname, lastname, year):
        super().__init__(fname, lastname)
        self.graduationyear = year


student1 = student("Arbaz", "Ansari", 2022)
print(student1.firstname, student1.lastname, student1.graduationyear)
