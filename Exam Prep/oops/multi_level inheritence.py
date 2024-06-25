class Gen1():
    def father(self):
        child1='Arbaz'
        child2='Arman'
        child3='Ashafq'
    def display(self):
        print(self.child1,self.child2,self.child3)
class Gen2(Gen1):
    def Arbaz(self):
        child1='A'
        child2='B'
    def display(self):
        print(self.child1,self.child2)
class Gen3(Gen2):
    def Arman(self):
        child1='C'
        child2='D'
    def display(self):
        print(self.child1,self.child2)

family=Gen3()
family.display()
family.Arbaz()
family.Arman()
