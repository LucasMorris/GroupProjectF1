import turtle

from model import Car


class TrackView:

    def __init__(self, canvas):
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

    def insertCar( self, car ):
        racecar = car
        racecar.startCar()









