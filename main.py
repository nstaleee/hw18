class Car:
    def __init__(self, producer, brand, year = 2020):
       self.producer = producer
       self.speedometr = 0
       self.brand = brand
       self.year = year

    def __str__(self):
        return f'Car {self.producer}'

    def __repr__(self):
        return f'Car {self.producer}'

    __repr__=__str__

audi = Car('audi', 'r8', 2022)
toyota = Car('toyota', 'Camry', 2021)
acura = Car('acura', 'nsx', 2019)


