# class Computers:
#     def hardware(self):
#         print("Mouse, KeyBoard, Touchpad, Scanner, etc.")
# class inputdevice(Computers):
#     def inputdevice1(self):
#         print("Mouse,Keyboard")
# hard=Computers()
# input1=inputdevice()
# hard.hardware()
# input1.inputdevice1()

# Another Code
class Animals:
    def speaks(self):
        print("Animals speaks")

class Dog(Animals):
    def bark(self):
        print("Dog Barking")

class childDog(Dog):
    def eat(self):
        print("Eat Breads")

d1=childDog()
d1.eat()
d1.bark()
d1.speaks()
