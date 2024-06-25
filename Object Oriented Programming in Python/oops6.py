class Car:
    def __init__(arbaz,modelname,year):
        arbaz.modelname=modelname
        arbaz.year=year
    def printfunc(abc):
        print("Car Model :",abc.modelname,"\nCar Model Year :",abc.year)

car1=Car("Fortuner",2022)
car1.printfunc()

