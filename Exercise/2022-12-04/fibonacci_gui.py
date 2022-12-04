'''
Author: Ethanlinyf e.yflin@gmail.com
Date: 2022-12-04 12:47:36
LastEditors: Ethanlinyf e.yflin@gmail.com
LastEditTime: 2022-12-04 14:18:06
FilePath: /Pokemon-Park/Preparation/Fabonacci/gui.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


#########################################
# Fibonacci Spiral                      #
# Davis MT                              #
# 2.11.2017                             #
# version 1.4                           #
#########################################

# import library
import turtle
import math

# setup Turtle
wn = turtle.Screen()
wn.setup(1000,800)
myTurtle = turtle.Turtle()  # set turtle to x = 0 and y = 0 on screen
myTurtle.pensize(3)


def main():             # this function calculate the value of fib and sends the results to the draw function
    valueOne = 0
    valueTwo = 1
    fib = 1
    for i in range(8):                      # number of squares to draw
        myTurtle.right(90)                  # point turtle to down position
        drawSq(fib*20)                      # call drawSq function-  argument = length of sides
        fib = valueOne + valueTwo           # calculate the value of Fibonacci
        valueOne = valueTwo
        valueTwo = fib
        
# this function draws the Fibonacci square
def drawSq(sides):
    for n in range(6):                     # the value 6 ensures that the start of the next square is correct
        myTurtle.forward(sides)            # draw the sides of the squares
        myTurtle.left(90)                  # turn pointer left 90 degrees


def sprial():
    r = 20                                 # draws to size of the radius
    angle = 90
    myTurtle.right(90)                     # turn turtle to down position
    myTurtle.penup()
    myTurtle.setpos(0,0)                   # move turtle to starting point of first square
    myTurtle.pendown()
    # draw fibonacci spiral
    arc(20, angle)                         # call arc function  1 * 20 = 20
    arc(20, angle)                         # call arc function  1 * 20 = 20
    arc(40, angle)                         # call arc function  2 * 20 = 40
    arc(60, angle)                         # call arc function  3 * 20 = 60
    arc(100, angle)                        # call arc function  5 * 20 = 100
    arc(160,angle)                         # call arc function 8 * 20 = 160
    arc(260,angle)                         # call arc function 13 * 20 = 260
    arc(420,angle)                         # call arc function 21 * 20 = 420


def arcLine(n, length, angle):            # Draws n line segments.
    for i in range(n):
        myTurtle.forward(length)
        myTurtle.left(angle)


def arc(r, angle):                        #  Draws an arc with the given radius and angle
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    # Before starting making a slight left turn.
    myTurtle.left(step_angle/2)
    arcLine(n, step_length, step_angle)
    myTurtle.right(step_angle/2)


# main program loop
main()                                     # calls the main function which draws the boxes
sprial()                                   # calls the spiral function which draws the sprial
wn.exitonclick()                           # click on the screen to exit the program
