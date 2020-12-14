class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self._width = _width

    weight = 25
    thickness = 5

    def findMass(self):
        mass = self._length * self._width * self.weight * self.thickness
        print(f"{self._length}м * {self._width}м * {self.weight}кг * {self.thickness}см = {mass}т")


a = Road(int(input("Длина = ")), int(input("Ширина = ")))
a.findMass()
