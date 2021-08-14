import turtle
a= turtle.Turtle()
     
b= 3
c= 70
d = 360.0 / b
for i in range(1000):
    for i in range(b):
        a.forward(c)
        a.right(d)
    b = b+1
    c = 70
    d = 360.0 / b
turtle.done()