import turtle as t
import random 

t.speed(0)
t.bgcolor("light blue")
def chao():
    t.penup()
    t.sety(-60)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("green")
    t.begin_fill()
    t.setheading(0)
    t.forward(1000)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(1000)
    t.end_fill()
    t.penup()
    
def casa():
    #Parede Frente
    t.pendown()
    t.setheading(0)
    t.pensize(2)
    t.pencolor("black")
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()

    #Parede Lado
    t.penup()
    t.forward(100)
    t.pendown()
    t.fillcolor("goldenrod")
    t.begin_fill()
    t.left(45)
    t.forward(60)
    t.setheading(270)
    t.forward(100)
    t.right(45)
    t.forward(60)
    t.end_fill()
    t.setheading(90)
    t.forward(100)
    t.penup()

    #Telhado 
    t.pendown()
    t.left(90)
    t.fillcolor("red")
    t.begin_fill()
    t.forward(100)
    t.right(90 + 30)
    t.forward(30)
    t.setheading(0)
    t.forward(70)
    t.right(60)
    t.forward(30)
    t.end_fill()

    #Telhado Lateral
    t.fillcolor("firebrick")
    t.begin_fill()
    t.setheading(0)
    t.left(45)
    t.forward(60)
    t.left(75)
    t.forward(30)
    t.left(105)
    t.forward(60)
    t.end_fill()
    t.setheading(0)
    t.right(60)
    t.forward(30)
    t.penup()

    #Telhado Superior
    t.fillcolor("red")
    t.begin_fill()
    t.setheading(0)
    t.back(100)
    t.left(60)
    t.forward(30)
    t.pendown()
    t.right(15)
    t.forward(60)
    t.setheading(0)
    t.forward(70)
    t.setheading(270)
    t.right(45)
    t.forward(60)
    t.right(45)
    t.forward(70)
    t.end_fill()

    t.left(60)
    t.forward(30)
    t.setheading(0)
    t.forward(100)
    t.penup()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(40)

    #porta
    t.pendown()
    t.fillcolor("sienna")
    t.begin_fill()
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.penup()


def flor():
    t.pendown()
    t.pensize(2)
    for i in range(6):
        t.fillcolor("pink")
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.right(60)

    t.penup()
    t.right(90)
    t.forward(4)
    t.left(90)
    t.pendown()

    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.penup()


def flores():
    x = random.randint(-800,800)
    y = random.randint(-400, -60)
    for i in range(50):
        t.setposition(x,y)
        flor()
        x = random.randint(-800,800)
        y = random.randint(-400, -60)
        


    


chao()
t.home()
flores()
t.home()
casa()
t.done()
