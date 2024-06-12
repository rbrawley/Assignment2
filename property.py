

class car():
    def __init__(self, year, make, model, engineSize):
        self.year = year
        self.make = make
        self.model = model
        self._engineSize = engineSize

    def Set_Engine_Size(self, newEngineSize):
        self._engineSize = newEngineSize

    def Get_Engine_Size(self):
        return self._engineSize

    engineSize = property(Get_Engine_Size, Set_Engine_Size)

car1 = car(2012, 'Nissan', 'Sentra', 1.5)

print(car1.engineSize)

car1.engineSize = 2.5

print(car1.engineSize)