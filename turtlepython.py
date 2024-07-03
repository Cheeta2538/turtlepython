import turtle
s =turtle.getscreen()
t = turtle.Turtle()
t.shape('turtle')
t.pen(pencolor="black", fillcolor="pink", pensize=10)
turtle.bgcolor("pink")
t.stamp()
for i in range (7):
    t.circle(100) 
    t.left(50)
