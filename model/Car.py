class Car:
    # fuel = 30
    speed = 10
    locX = 0
    locY = 30
    # engine = 2 # default engine
    # tires = 3 # supersoft

    def __init__(self, locX, locY, speed):
        self.locX = locX
        self.locY = locY
        self.speed = speed

    def updateCar(self, speed, locX, locY):
        self.speed = speed
        self.locX = locX
        self.locY = locY
