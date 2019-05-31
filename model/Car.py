import turtle


class Car:
    # fuel = 30
    speed = 10
    locX = 0
    locY = 30
    # engine = 2 # default engine
    # tires = 3 # supersoft

    def __init__(self):
        self.locX = 0
        self.locY = 30
        self.speed = 10

    def updateCar(self, speed, locX, locY):
        self.speed = speed
        self.locX = locX
        self.locY = locY

    def startCar(self):
        raceCar = turtle.Turtle()
        raceCar.color("red")
        raceCar.shape("triangle")

        raceCar.up()
        raceCar.goto(0, -125)

        raceCar.forward(100)
        raceCar.circle(125, 180)
        raceCar.forward(200)
        raceCar.circle(125, 180)
        raceCar.forward(100)
