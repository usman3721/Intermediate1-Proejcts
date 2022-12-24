from turtle import Turtle,Screen
pro=Turtle()


screen=Screen()
def forward():
    pro.forward(5)
def backward():
    pro.backward(5)
def left():
    pro.left(5)
def right():
    pro.right(5)
def clear():
    pro.clear() 
    pro.penup()
    pro.home()   
    pro.pendown()



screen.listen()
screen.onkeypress(key="w",fun=forward)
screen.onkeypress(key="s",fun=backward)
screen.onkey(key="a",fun=left)
screen.onkey(key="d",fun=right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()