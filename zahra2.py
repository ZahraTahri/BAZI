import turtle
import random
import winsound
Score=0
s =turtle.Screen()
s.setup(600,600)
s.title("بازی پاندا و دونات")
s.bgpic('bacz.gif')
 # دیوار
wall=turtle.Turtle()
wall.up()
wall.goto(-275,275)
wall.down()
wall.width(5)
for i in range (4):
    wall.fd(550)
    wall.rt(90)
wall.ht()

# شخصیت بازی
panda=turtle.Turtle()
s.register_shape('panda2.gif')
panda.shape('panda2.gif')
panda.up()
# دونات
ball=turtle.Turtle()
s.register_shape("dn1.gif")
ball.shape("dn1.gif")
ball.up()
ball.goto(random.randint(-260,260),random.randint(-260,260))
# امتیاز
wr=turtle.Turtle()
wr.up()
wr.goto(-270,275)
wr.ht()
wr.color('black')
wr.write('امتیاز = ' + str(Score),font=('b koodak',16,'bold'))



# توابع حرکت
def move_right():
    panda.right(90)
def move_left():
     panda.left(90)
def move_up():
    panda.seth(90)
    panda.fd(20)
def move_down():
    panda.seth(270)
    panda.fd(20)
s.listen()
s.onkey(move_right,'Right' )
s.onkey(move_left,'Left')
s.onkey(move_up,'Up')
s.onkey(move_down,'Down')

#مانع
oo=turtle.Turtle()
s.register_shape("oo.gif")
oo.shape("oo.gif")
oo.up()
oo.goto(random.randint(-260,260),random.randint(-260,260))
oo_x, oo_y = random.randint(-75, 75), random.randint(-75, 75)
while abs(panda.xcor() - oo_x) < 50 and abs(panda.ycor() - oo_y) < 50:
    oo_x, oo_y = random.randint(-75, 75), random.randint(-75, 75)
oo.goto(oo_x, oo_y)

#در حال حرکت
while True:
    panda.fd(1)
    if panda.xcor()>270 or panda.xcor()<-270 or panda.ycor()>270 or panda.ycor()<-270:
        panda.right(180)
        Score=Score-5
        wr.clear()
        wr.write('امتیاز = ' + str(Score),font=('b koodak',12,'bold'))
        winsound.Beep(1000, 300)
    if panda.distance(oo) < 25:
        oo.goto(random.randint(-260, 260), random.randint(-260, 260))
        oo.goto(random.randint(-260, 260), random.randint(-260, 260))

        Score = Score -5
        wr.clear()
        wr.write('امتیاز = ' + str(Score), font=('b koodak', 12, 'bold'))

    if panda.distance(ball)<15:
        ball.goto(random.randint(-260,260),random.randint(-260,260))
        Score = Score +10
        wr.clear()
        wr.write('امتیاز = ' + str(Score),font=('b koodak',12,'bold'))
    if Score>=40:
        wr.goto(+50,-50)
        wr.write('آفرین شما برنده شدید :)' , font=('b koodak',18,'bold'))
    if Score<=-10:
        wr.goto(-75, 0)
        wr.write('،، متاسفم شما باختید :) ،، ', font=('b koodak', 18, 'bold'))

        break

turtle.mainloop()