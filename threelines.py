#Patti Crosswait
#threelines.py

import turtle as t

wn = t.Screen()

a = t.Turtle()

a.pensize(3)
a.pd()
a.back(200)
a.lt(90)
a.pu()

a.fd(30)
a.pd()
a.rt(90)
a.fd(200)
a.pu()

a.lt(90)
a.fd(30)
a.lt(90)
a.pd()
a.fd(200)

wn.exitonclick()