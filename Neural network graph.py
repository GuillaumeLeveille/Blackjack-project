import math
import turtle as t

from numpy import array, random, exp, dot

t.hideturtle()
num = 3
names = ('winning move','hand value','losing move' )
t.penup()
t.forward(200)
t.pendown()
t.circle(30)
t.penup()
t.forward(-200)
t.pendown()
t.circle(30)
t.write(chr(931), font=('Arial', 32, 'normal'))
degree = 165 - num * 10
t.left(135)
t.penup()
t.forward(math.sqrt(2) * 30)
t.pendown()
pt = t.position()
i = 0
while i < num:
    t.forward(150)
    t.right(90)
    t.circle(20)
    t.write('w' + str(i))
    t.left(90)
    t.forward(150)
    t.right(90)
    t.circle(20)
    t.write(names[i])
    t.goto(pt)
    t.left(degree)
    i += 1
t.goto(200, pt[1])
t.write('hit or stay ')
t.goto(300, 200)
t.circle(20)
t.write("hit")
t.goto(200,pt[1])
t.goto(300,-200)
t.circle(20)
t.write("stay")
input('PRESS ANY KEY TO STOP...')
