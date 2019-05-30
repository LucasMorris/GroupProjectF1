import turtle

racetrack = turtle.Screen()

outerborder = turtle.Turtle()
outerborder.color("black", "grey") #stroke colour and fill colour
innerborder = turtle.Turtle()
innerborder.color("black", "olive")
racecar = turtle.Turtle()
racecar.color("red")
racecar.shape("turtle")

# Turtle drawing speed
outerborder.speed()
innerborder.speed()

outerborder.up()
outerborder.goto(0, -150)
outerborder.down()

innerborder.up()
innerborder.goto(0, -100)
innerborder.down()

outerborder.begin_fill()
outerborder.forward(100)
outerborder.circle(150, 180)
outerborder.forward(200)
outerborder.circle(150, 180)
outerborder.forward(100)
outerborder.end_fill()

innerborder.begin_fill()
innerborder.forward(100)
innerborder.circle(100, 180)
innerborder.forward(200)
innerborder.circle(100, 180)
innerborder.forward(100)
innerborder.end_fill()

racecar.up()
racecar.goto(0, -125)

racecar.forward(100)
racecar.circle(125, 180)
racecar.forward(200)
racecar.circle(125, 180)
racecar.forward(100)

racetrack.exitonclick()
