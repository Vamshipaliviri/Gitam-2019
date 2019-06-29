#generation of symbol using python turtle
from turtle import*
def main():
    colors=["red","yellow","orange","green","blue","seagreen","royalblue"]
    reset()
    Screen()
    up()
    goto(-320,-195)
    width(70)
    for pcolor in colors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)
    width(25)
    color("white")
    goto(0,-170)
    down()

    circle(170)
    #goto(0,80)
    left(90)
    forward(340)
    up()
    left(180)
    forward(170)
    right(45)
    down()
    forward(170)
    up()
    backward(170)
    left(90)
    down()
    forward(170)

main()
    
