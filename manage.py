import turtle as tr
import colorsys as cs

# Screen setup
tr.setup(width=800, height=700)
tr.speed(0)
tr.tracer(10)
tr.width(2)
tr.bgcolor("black")

# Move the turtle to the center of the screen and add a small offset
# tur.penup()
tr.teleport(-150, 250)  # Adjust coordinates to center the drawing on the screen
# tur.pendown()

# Start drawing
for j in range(26):
    for i in range(15):
        tr.color(cs.hsv_to_rgb(i / 15, j / 26, 1))
        tr.right(90)
        tr.circle(200 - j * 4, 90)
        tr.left(90)
        tr.right(180)
        tr.circle(200 - j * 4, 90)
        tr.right(180)
        tr.circle(60, 24)

tr.hideturtle()
tr.done()
