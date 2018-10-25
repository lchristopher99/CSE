# Name: Logan Christopher Date Assigned: 9-19-18
#
# Course: CSE 1284 Sec 11 Date Due: 9-22-18
#
# File name: Fill in
#
# Program Description: Brief description of what the program does.

import turtle 

# Gathering user input for necessary variables
bottom_left_x = int(input('Enter bottom left x: '))
bottom_left_y = int(input('Enter bottom left y: '))
width = int(input('Enter rectangle width: '))
height = int(input('Enter rectangle height: '))
pointX = int(input('Enter point x: '))
pointY = int(input('Enter point y: '))

# Assigning turtle color and navigating to point of origin
turtle.color('green')
turtle.penup()
turtle.goto(bottom_left_x, bottom_left_y)
turtle.pendown()

# Adding width to point of origin to determine point 2
width = bottom_left_x + width

# Navigating to point 2
turtle.goto(width, bottom_left_y)

# Adding height to point of origin to determine point 3
height = bottom_left_y + height

# Navigating to point 3 using new vars that were defined above
turtle.goto(width, height)

# Navigating to point 4 using new vars that were defined above
turtle.goto(bottom_left_x, height)

# Returning turtle back to point of origin to complete rectangle
turtle.goto(bottom_left_x, bottom_left_y)

# Picking up pen and moving turtle to random point determined from user input
turtle.penup()

# Reassigning turtle color
turtle.color('blue')
turtle.goto(pointX, pointY)
turtle.pendown()

# Determining whether turtle is on, in, or outside the rectangle
if bottom_left_x <= pointX <= width and bottom_left_y <= pointY <= height:
  if bottom_left_x <= pointX <= width and pointY == bottom_left_y:
    print('On bottom line')
  else:
    if bottom_left_x <= pointX <= width and pointY == height: 
      print('On top line')
    else:
      if bottom_left_y <= pointY <= height and pointX == width:
        print('On right side line')
      else:
        if bottom_left_y <= pointY <= height and pointX == bottom_left_x:
          print('On left line')
        else:
          print('Inside rectangle')
else:
  print('Outside')

turtle.done()