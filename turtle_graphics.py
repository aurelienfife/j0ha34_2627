import turtle

battery = 65
colour = "grey"
message = "Battery level"

# PLACEHOLDER CODE HERE: replace this comment with your selection code.

turtle.setup(500, 300)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 30)
turtle.dot(100, colour)
turtle.goto(0, -60)
turtle.write(message, align="center", font=("Arial", 16, "normal"))
turtle.done()