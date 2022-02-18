from turtle import *

# speed(11)
# n = 1
# while True:
#     forward(n)
#     left(90)
#     color()
#     right(45)
#     n = n+5

##########################

color('green')
bgcolor('black')
speed(11)
hideturtle()
b = 0
while b < 100:
    right(b)
    forward(b * 3)
    b = b + 1

