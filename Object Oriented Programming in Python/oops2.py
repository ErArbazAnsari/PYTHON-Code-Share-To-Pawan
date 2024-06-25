class Employee:
    company="Youtube"

harry=Employee()
rohan=Employee()

harry.name='Harry'
harry.salary='20000'
harry.company='Google'
rohan.name='Rohan'
rohan.salary='20000'

print(harry.name,harry.salary,harry.company)
print(harry.__dict__)
print(rohan.name,rohan.salary,rohan.company)
print(rohan.__dict__)
print(Employee.__dict__)
