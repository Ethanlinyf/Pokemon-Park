
# import library
import turtle
import math

# setup Turtle
wn = turtle.Screen()
wn.setup(1000,800)
myTurtle = turtle.Turtle()  # set turtle to x = 0 and y = 0 on screen
myTurtle.pensize(3)


def main():             # this function calculate the value of fib and sends the results to the draw function
                 # number of squares to draw
        myTurtle.right(90)                  # point turtle to down position
        drawSq(20)                      # call drawSq function-  argument = length of sides

        
# this function draws the Fibonacci square
def drawSq(sides):
    for n in range(6):                     # the value 6 ensures that the start of the next square is correct
        myTurtle.forward(sides)            # draw the sides of the squares
        myTurtle.left(90)                  # turn pointer left 90 degrees


# main program loop
main()                                     # calls the main function which draws the boxes
# sprial()                                   # calls the spiral function which draws the sprial
wn.exitonclick()        