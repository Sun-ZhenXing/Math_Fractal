# -*- coding: utf-8 -*-
import turtle

Division = 3.0 
DirectionAangle = [('left',60),('right',120),('left',60)]

def call(name):
    if name == 'left':
        return turtle.left
    else:
        return turtle.right

def koch(n, length):
    if n==0:
        turtle.forward(length)   
    else:
        for DA in DirectionAangle:
            koch(n-1,length/Division)
            call(DA[0])(DA[1])
        koch(n-1,length/Division)   

koch(n=6, length=5000)
turtle.done()