import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle

alex.color("green")    # draws a circle of radius 50
#draws circles
for counter in range(1,5):
    alex.circle(20*counter)

alex.color("blue")    # alex has a color
alex.right(120)        # draws a circle of radius 50
#draws circles
for counter in range(1,5):
    alex.circle(20*counter)
alex.color("red")    # alex has a color
alex.right(120)         # draws a circle of radius 50
#draws circles
for counter in range(1,5):
    alex.circle(20*counter)

#Write the logic to create the given pattern
#Refer the statements given above to draw the pattern
