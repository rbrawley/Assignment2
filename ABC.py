from abc import ABC , abstractmethod

class vehicle(ABC):
    @abstractmethod
    def Set_Engine_Size(self, newTireSize):
        pass

    @abstractmethod
    def GetES(self):
        pass
    
class car(vehicle):
    def __init__(self, year, make, model, engineSize):
        self.year = year
        self.make = make
        self.model = model
        self.engineSize = engineSize

    def Set_Engine_Size(self, newEngineSize):
        self.engineSize = newEngineSize

    def GetES(self):
        pass

car1 = car(2001, 'ford', 'f150', 5.4) 

print(car1.GetES)

car1.Set_Engine_Size = 3.6 

print(car1.GetES)        