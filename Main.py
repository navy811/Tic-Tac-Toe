import turtle

t=turtle.Turtle()

screen = turtle.Screen()

screen.setup(1000,700)

screen.bgcolor('red')

t.penup()
t.setpos(-170,300)

t.write('KOLKO I KRZYZYK',font=('Arial',30,'bold'))

#siatka
t.speed(10)
t.pensize(5)
t.setpos(-300,100)
t.pendown()
t.forward(600)
t.penup()
t.setpos(-300,-50)
t.pendown()
t.forward(600)
t.penup()
t.setpos(-100,250)
t.pendown()
t.right(90)
t.forward(450)
t.penup()
t.setpos(100,250)
t.pendown()
t.forward(450)
t.penup()

x=-470
y=330

#ozdoby
# for i in range(4):
#     t.setpos(x,y)
#     t.pendown()
#     t.left(45)
#     t.forward(100)
#     t.left(135)
#     t.penup()
#     t.forward(71)
#     t.left(135)
#     t.pendown()
#     t.forward(100)
#     t.penup()
#     t.left(45)
#     y -= 200
#     t.setpos(x,y)
#
# x=370
# y=230
# for i in range(4):
#     t.setpos(x,y)
#     t.pendown()
#     t.left(45)
#     t.forward(100)
#     t.left(135)
#     t.penup()
#     t.forward(71)
#     t.left(135)
#     t.pendown()
#     t.forward(100)
#     t.penup()
#     t.left(45)
#     y -= 200
#     t.setpos(x,y)
#
# x=-470
# y=160
# for i in range(4):
#     t.setpos(x,y)
#     t.pendown()
#     t.left(45)
#     t.circle(50)
#     y-=200
#     x+=35
#     t.penup()
# x= 440
# y= 330
# for i in range(5):
#     t.setpos(x,y)
#     t.pendown()
#     t.left(45)
#     t.circle(50)
#     y-=200
#     x-=35
#     t.penup()
licznik_ruchow = 0
licznik_x =0
def ruch(a,b):
    global licznik_ruchow
    global licznik_x
    if licznik_ruchow%2==0:
        t.penup()
        t.setheading(0)
        t.setpos(a,b)
        t.pendown()

        t.left(45)
        t.forward(50)
        t.setheading(90)
        t.setpos(a,b)

        t.left(45)
        t.forward(50)
        t.setheading(270)
        t.setpos(a, b)

        t.right(45)
        t.forward(50)
        t.setheading(270)
        t.setpos(a, b)

        t.left(45)
        t.forward(50)
        t.setpos(a, b)
        t.setheading(90)

        licznik_ruchow += 1
    else:
        t.penup()
        t.setpos(a, b)
        t.pendown()
        t.circle(50)
        t.penup()
        licznik_ruchow += 1
screen.onclick(ruch)


















turtle.mainloop()