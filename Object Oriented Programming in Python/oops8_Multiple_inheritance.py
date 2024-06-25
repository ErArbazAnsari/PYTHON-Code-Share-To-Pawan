class cal1:
    def sum(self,a,b):
        return a+b
class cal2:
    def minus(self,a,b):
        return a-b
class cal3():
    def mul(self,a,b):
        return a*b
class Calculator(cal1,cal2,cal3):
    def divi(self,a,b):
        return a/b

calc=Calculator()
print(calc.sum(10,20))
print(calc.minus(10,20))
print(calc.mul(10,20))
print(calc.divi(10,20))
print(issubclass(Calculator,cal1))
print(issubclass(Calculator,cal2))
print(issubclass(Calculator,cal3))
print(issubclass(cal2,cal1))
print(issubclass(cal3,Calculator))
print(isinstance(calc,cal2))