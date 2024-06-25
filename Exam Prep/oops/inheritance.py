class Animals():
    def speaking(self):
        print('animal speaking')

class newanimal(Animals):
    def dog(self):
        print('dog is barking')

animal=newanimal()
animal.dog()
animal.speaking()