import turtle

from model import Car


class TrackView:
    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas

        outerBorder = turtle.RawTurtle(canvas)
        outerBorder.color("black", "grey") #stroke colour and fill colour
        innerBorder = turtle.RawTurtle(canvas)
        innerBorder.color("black", "olive")

        # Turtle drawing speed
        outerBorder.speed(0)
        innerBorder.speed(0)

        outerBorder.up()
        outerBorder.goto(0, -150)
        outerBorder.down()

        innerBorder.up()
        innerBorder.goto(0, -100)
        innerBorder.down()

        outerBorder.begin_fill()
        outerBorder.forward(100)
        outerBorder.circle(150, 180)
        outerBorder.forward(200)
        outerBorder.circle(150, 180)
        outerBorder.forward(100)
        outerBorder.end_fill()
        outerBorder.hideturtle()

        innerBorder.begin_fill()
        innerBorder.forward(100)
        innerBorder.circle(100, 180)
        innerBorder.forward(200)
        innerBorder.circle(100, 180)
        innerBorder.forward(100)
        innerBorder.end_fill()
        innerBorder.hideturtle()

    def insertCar( self, car):
        self.driveCar(car)

    def driveCar(self, car):
        raceCar = turtle.RawTurtle(self.canvas)
        raceCar.color("red")
        raceCar.shape("triangle")

        raceCar.up()
        raceCar.goto(0, -125)

        while(1):
            raceCar.forward(100)
            raceCar.circle(125, 180)
            raceCar.forward(200)
            raceCar.circle(125, 180)
            raceCar.forward(100)
