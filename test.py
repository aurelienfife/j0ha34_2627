import turtle

screen = turtle.Screen()
screen.setup(900, 700)
screen.title("Fibonacci spiral")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.color("blue")

pen.penup()
pen.goto(-100, -80)
pen.pendown()
pen.dot(10, "red")

a, b = 1, 1

for step in range(10):
    pen.circle(a * 4, 90)
    a, b = b, a + b

screen.update()
screen.mainloop()