import turtle

battery = 15
colour = "grey"
message = "Battery level"

# PLACEHOLDER CODE HERE: replace this comment with your selection code.
if battery < 0 or battery > 100:
    colour = "grey"
    message = "Invalid battery level"
elif battery < 20:
    colour = "red"
    message = "Charge now!"
elif battery < 60:
    colour = "orange"
    message = "Battery okay"
else:
    colour = "green"
    message = "Battery good"

turtle.setup(500, 300)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 30)
turtle.dot(100, colour)
turtle.goto(0, -60)
turtle.write(message, align="center", font=("Arial", 16, "normal"))
turtle.done()