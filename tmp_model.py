class Car():
    fuel = 30
    speed = 10
    locX = 0
    locY = 30
    engine = 2 # default engine
    tires = 3 # supersoft

    def updateCar(speed, fuel, locX, locY, engine, tires):
        self.speed = speed
        self.fuel = fuel
        self.locX = locX
        self.locY = locY
        self.engine = engine
        self.tires = tires
