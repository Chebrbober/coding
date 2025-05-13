import turtle

# Создание окна
screen = turtle.Screen()
screen.screensize(1000,1000)
screen.bgcolor("black")

# Создание границ для игрока
border = turtle.Turtle()
border.up()
border.setposition(-100, -300,)
border.down()
border.color("white")
border.pensize(10)
border.speed(15)
for side in range(4):
    border.forward(200)
    border.left(90)
border.hideturtle()

# Создание игрока черепаха
player = turtle.Turtle()
player.color("red")
player.shape("square")
player.up()
player.setposition(0, -150)
player.speed(0)

# Скорость игрока
speed = 1

# Создание функций

def turn_left():
    player.setheading(180)

def turn_right():
    player.setheading(0)

def move_forward():
    player.setheading(90)

def move_backward():
    player.setheading(-180)




# Назначение клавиш
turtle.listen()
turtle.onkeypress(turn_left, "Left")
turtle.onkeypress(turn_right, "Right")
turtle.onkeypress(move_forward, "Up")



while True:
    player.forward(speed)

    # Если игрок за границей
    if player.xcor() > 90 or player.xcor() < -90:
        player.right(180)
    if player.ycor() > -110 or player.ycor() < -280:
        player.right(180)






#delay = raw_input("Press Enter to finish.")