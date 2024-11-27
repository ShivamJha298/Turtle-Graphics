# Draw a Ninja - Ninja Design in Python 
''' “Turtle” is a Python feature (Graphics-Library) like a drawing board, which lets us command a turtle to draw all over it! We can use functions like turtle.forward(…) and turtle.right(…) which can move the turtle around. '''                                             
import turtle
ninja = turtle.Turtle()    # Creating a turtle instance
ninja.speed(10)            # Setting the speed

for i in range(180):
    ninja.forward(100)     # moves the turtle forward by 100 units.
    ninja.right(30)        # rotates the turtle right by 30 degrees
    ninja.left(60)         # rotates the turtle left by 60 degrees
    ninja.forward(50)      # moves the turtle forward by 50 units.
    ninja.right(30)        # rotates the turtle right by 30 degrees
    ninja.penup()          # Lifts the pen, so moving to a new position won't draw a line.
    ninja.setposition(0, 0) # Restarts the turtle position to the centre of the scren (co-ordinates (0,0)).
    ninja.pendown()       # Lowers the pen down, so the turtle can draw once again.
    ninja.right(2)        # rotates the turtle right by 2 degrees, changing the direction slightly for the next iteration.
