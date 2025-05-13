import turtle
turtle.shape("turtle")
for y in range(0,241,60):
    turtle.goto (0,y)
    for i in range (5):
        turtle.down ()
        turtle.circle (30)
        turtle.up()
        turtle.forward (60)
