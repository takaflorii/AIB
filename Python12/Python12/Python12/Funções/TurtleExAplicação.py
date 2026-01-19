import turtle
desenho=turtle.Turtle()
lado=int(200)

for n in range(4):
    desenho.forward(lado)
    desenho.left(90)
    
turtle.reset()

turtle.goto(0, 0)
desenho2= turtle.Turtle()
for n in range(3):
    desenho2.forward(150)
    desenho2.right(120)
    desenho2.speed(1)
    
turtle.reset()

t = turtle.Pen()
t.penup()
x=40
y=40
t.setpos(x,y)
t.pendown()
for m in range(100):
    t.forward(m*2)
    t.left(91)