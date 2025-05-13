import turtle
for i in range (1,11):
    turtle.up()
    turtle.goto(-20*1,-20*i)
    turtle.down()
    for j in range(i):
        for k in range (2):
            turtle.forward (40)
            turtle.right (90)
            turtle.forward (20)
            turtle.right (90)
        turtle.forward (40)
