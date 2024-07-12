import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Create a turtle object
tux = turtle.Turtle()
tux.speed(0)  # Set the speed to the fastest

# Draw the body
tux.penup()
tux.goto(0, -250)
tux.pendown()
tux.begin_fill()
tux.color("black")
tux.circle(200)
tux.end_fill()

# Draw the belly
tux.penup()
tux.goto(0, -200)
tux.pendown()
tux.begin_fill()
tux.color("white")
tux.circle(160)
tux.end_fill()

# Draw the head
tux.penup()
tux.goto(0, 0)
tux.pendown()
tux.begin_fill()
tux.color("black")
tux.circle(120)
tux.end_fill()

# Draw the eyes
tux.penup()
tux.goto(-40, 70)
tux.pendown()
tux.begin_fill()
tux.color("white")
tux.circle(30)
tux.end_fill()

tux.penup()
tux.goto(40, 70)
tux.pendown()
tux.begin_fill()
tux.circle(30)
tux.end_fill()

# Draw the pupils
tux.penup()
tux.goto(-40, 90)
tux.pendown()
tux.begin_fill()
tux.color("black")
tux.circle(15)
tux.end_fill()

tux.penup()
tux.goto(40, 90)
tux.pendown()
tux.begin_fill()
tux.circle(15)
tux.end_fill()

# Draw the beak
tux.penup()
tux.goto(0, 50)
tux.pendown()
tux.begin_fill()
tux.color("orange")
tux.left(45)
for _ in range(2):
    tux.forward(80)
    tux.right(90)
tux.end_fill()

# Draw the feet
tux.penup()
tux.goto(-100, -300)
tux.pendown()
tux.begin_fill()
tux.color("orange")
for _ in range(2):
    tux.forward(120)
    tux.right(90)
    tux.forward(50)
    tux.right(90)
tux.end_fill()

# Hide the turtle and display the result
tux.hideturtle()
screen.mainloop()

