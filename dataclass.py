from dataclasses import dataclass
@dataclass
class Car:
    brand: str
    year: int
    engineSize: float


car1 = Car('Ford', 2001, 2.4) 

print(car1.engineSize)

car1.engineSize = 3.6 

print(car1.engineSize)