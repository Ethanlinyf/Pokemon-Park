
import turtle
import math

wn = turtle.Screen()
wn.setup(1000,800)
myTurtle = turtle.Turtle()
myTurtle.pensize(3)

def draw_square(side):
    for i in range(6):
        myTurtle.forward(side)
        myTurtle.left(90)

def sprial():
    r = 20                                 
    angle = 90
    myTurtle.right(90)                     
    myTurtle.penup()
    myTurtle.setpos(0,0)
    # draw fibonacci spiral
    myTurtle.pendown()  
    myTurtle.pencolor("red")
    arc(20, angle)                         
    arc(20, angle)                         
    arc(40, angle)                         
    arc(60, angle)                         
    arc(100, angle)                        
    arc(160,angle)                         
    arc(260,angle)                         
    arc(420,angle)                         

def arcLine(n, length, angle):            
    for i in range(n):
        myTurtle.forward(length)
        myTurtle.left(angle)

def arc(r, angle):                        
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    # Before starting making a slight left turn.
    myTurtle.left(step_angle/2)
    arcLine(n, step_length, step_angle)
    myTurtle.right(step_angle/2)

def main():
    valueOne = 0
    valueTwo = 1
    fib = 1
    for i in range(8):                      
        myTurtle.right(90)                  
        draw_square(fib*20)                  
        fib = valueOne + valueTwo           
        valueOne = valueTwo
        valueTwo = fib

if __name__ == "__main__":
    main()
    sprial()
    wn.exitonclick()