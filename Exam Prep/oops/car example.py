class Car:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def display(self):
        print("Model of the Car is",self.model,'and year of the is',self.year)

model=input('Enter Model Name of car : ')
year=input('Enter year of car : ')

car1=Car(model,year)
car1.model='Toyota'
# del car1.model ----> use for deleting the attributes
# del car1.model
# print(car1.model)
car1.display()
