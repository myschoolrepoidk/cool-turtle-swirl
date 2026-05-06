from turtle import *
from math import *
from random import *
pensize(4)
Turtle.speed = 1000
i=1
j=100
v=""
while 1==1:
    x = randint(0,2)
    if x==0:
        v='blue'
    elif x==1:
        v='CornflowerBlue'
    elif x==2:
        v='azure2'
    pencolor(v)
    goto(cos(i)*j,sin(i)*j)
    i = i+1
    j=j-0.1
