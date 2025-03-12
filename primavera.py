import turtle

def draw_tulip():
    turtle.bgcolor("lightblue")

    # Dibuja la flor
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.circle(50, 180)
    turtle.right(180)
    turtle.circle(50, 180)
    turtle.forward(100)
    turtle.end_fill()

    # Dibuja el tallo
    turtle.color("green")
    turtle.right(90)
    turtle.width(5)
    turtle.forward(200)

    # Dibuja las hojas
    turtle.right(90)
    turtle.color("darkgreen")
    turtle.begin_fill()
    turtle.circle(30, 180)
    turtle.right(180)
    turtle.circle(30, 180)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

draw_tulip()

