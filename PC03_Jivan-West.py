'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Jivan West
September 11, 2020

This program creates a background for zoom using concentric circles and other types of repeating circles 
'''

from turtle import * #import the library of commands that you'd like to use
import math #get a bunch of math commands

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#=======Add your code here======
clear()
setheading(90)
speed(100)
yellow = (249, 199, 79)
green = (144, 190, 109)
seafoam = (67, 170, 139)
mint = (130, 166, 177)
offwhite = (253, 252, 220)
palette = [yellow, green, seafoam, offwhite, mint]
bgcolor([45,45,45])
REPEATS = range(18)
radius = 20
number = 10

#background spirals
color([135,165,135])
up()
goto(35,10)
down()
pensize(3)
for i in range(420):
  circle(35+i, 10)
  
#up() 
#goto(-100,-150)
#down()
#egin_fill()
#color("black")
#circle(200)
#end_fill()
  
#kelp colored ovals
begin_fill()
up()
goto(0,0)
down()
kelp = (132, 213, 199)
color(kelp)
begin_fill()
for element in range(number): 
    setheading(0)
    circle(radius)
    setheading(180)
    circle(radius)
    radius = radius+35
end_fill()


#mint wings
up()
goto(0,0)
down()
color(palette[4])
begin_fill()
for element in range(number): 
    setheading(90)
    circle(radius)
    setheading(270)
    circle(radius)
    radius = radius+20
   
#green wings
goto(0,0)
down()
color(palette[1])
begin_fill()
for element in range(number): 
    setheading(90)
    circle(radius)
    setheading(270)
    circle(radius)
    radius = radius+20
    
end_fill()

#sector bot
#up()
#goto(-140,-75)
#down()
#setheading(90)
#darkgren = (117, 142, 79)
#color(darkgren)
#circle(200,90)


#color([255,255,255])
#goto(-7,-2)
#for i in range(52):
  # forward(200)
   #left(175)
   #forward(200)
   #left(90)
   #forward(20)
   #left(90)
   #right(2)
   
begin_fill()
color([235,255,255])
up()
goto(-500,-2)
down()
for i in range(52):
   forward(200)
   left(175)
   forward(200)
   left(90)
   forward(20)
   left(90)
   right(2)
end_fill()

begin_fill()
color([235,255,255])
up()
goto(500,-2)
down()
for i in range(52):
   forward(200)
   left(175)
   forward(200)
   left(90)
   forward(20)
   left(90)
   right(2)

end_fill()



