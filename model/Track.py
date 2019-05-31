class Track:
    name: None
    cars = []

    def __init__(self, name):
        self.name = name


    def insertCar(self, car):
        self.cars.append(car)

