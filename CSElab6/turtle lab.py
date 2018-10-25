#Name: Jason Hwang, Travis Taliancich, Logan Christopher, Rees Hogue    Date Assigned: 10/19/2018
#
#Course: CSE 1284 Section 14                                            Date Due: 10/20/2018
#
#File name: Geometry
#
#Program Description: Make a geometric shape


#This is the function for making the circle using turtle
    
def draw_circle(x, y, r):
    import turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)
    turtle.penup()

#This is the function for making the rectangle using turtle

def draw_rectangle(x, y, width, height):
    import turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.penup()

#This is the function for making the point using turtle
    
def draw_point(x, y, size):
    import turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(size)
    turtle.left(180)
    turtle.forward(size * 2)
    turtle.left(180)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(180)
    turtle.forward(size * 2)

#This is the function for making the line using turtle

def draw_line(x1, y1, x2, y2):
    import turtle
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()

#This is the function for making the triangle using turtle.

def draw_triangle(x, y, side):
    import turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.penup()
    
#the function that will call all of the functions
    
def main():
    draw_circle(-100, -100, 200)
    draw_circle(100, 100, 200)
    draw_rectangle(10, 10, 50, 70)
    draw_rectangle(90, 90, 100, 150)
    draw_point(0, 0, 50)
    draw_point(70, 70, 50)
    draw_line(20, 20, 30, 70)
    draw_line(300, 200, 100, 150)
    draw_triangle(100, 100, 50)
    draw_triangle(-100, -150, 50)

main()
