import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

alex.speed(1)

alex.write("Welcome to COMP123",
           True,
           "left",
           ('Arial', 20, 'bold'))

wn.exitonclick()
