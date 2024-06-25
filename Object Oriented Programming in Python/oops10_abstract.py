from abc import ABC
class polygon(ABC):
    def sides(self):
        pass
class sqare(polygon):
    def sides(self):
        print("sqare have 4 sides")
class pentagon(polygon):
    def sides(self):
        print("pentagon have 5 sides")
class hexagon(polygon):
    def sides(self):
        print("hexagon have 6 sides")
class septagon(polygon):
    def sides(self):
        print("septagon have 7 sides")
sqares=sqare()
print(sqares.sides())
pentagons=pentagon()
print(pentagons.sides())
hexagons=hexagon()
print(hexagons.sides())
septagons=septagon()
print(septagons.sides())
