class Employee:
    def __int__(self,ename,eid,salary,epost):
        self.ename=ename
        self.eid=eid
        self.salary=salary
        self.epost=epost
    def display(self):
        print('Emp Name is',self.ename,'Emp Eid is',self.eid,'Salary is',self.salary,'Post is',self.epost)

# Attributes Creation
em1=Employee("Arbaz",24018,20000,"Manager")
emp1.display()