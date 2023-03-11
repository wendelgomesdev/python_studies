from dataclasses import dataclass
# Usamos essa biblioteca quando criamos classes de dados (classes que não possuem metodos)

@dataclass
class Car:
    name: str
    color: str
    model: str
    brand: str
    price: float

a = Car('fiesta', 'white', '2010', 'ford', 35000)
b = Car('civic', 'black', '2014', 'honda', 25000)
print(a == b)