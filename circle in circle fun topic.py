from turtle import *

i = 1
bgcolor("black")
speed(0)
hideturtle()
while i <= 200:
    color("red")
    circle(i)
    color("orange")
    circle(i*0.8)
    right(3)
    forward(3)
    i += 1
done()