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
donat=turtle.Turtle()
s.register_shape("dn1.gif")
donat.shape("dn1.gif")
donat.up()
donat.goto(random.randint(-260,260),random.randint(-260,260))
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

def show_winner_screen():
    s.clear()  # پاک کردن صفحه فعلی
    s.bgpic('bord.gif')  # نمایش عکس برنده شدن
    s.exitonclick()


#در حال حرکت
while True:
    panda.fd(1)
    if panda.xcor()>270 or panda.xcor()<-270 or panda.ycor()>270 or panda.ycor()<-270:
        panda.right(180)
        Score=Score-5
        wr.clear()
        wr.write('امتیاز = ' + str(Score),font=('b koodak',12,'bold'))
        winsound.PlaySound('divar.wav', winsound.SND_FILENAME)






    if panda.distance(oo) < 25:
        oo.goto(random.randint(-260, 260), random.randint(-260, 260))
        oo.goto(random.randint(-260, 260), random.randint(-260, 260))

        Score = Score -5
        wr.clear()
        wr.write('امتیاز = ' + str(Score), font=('b koodak', 12, 'bold'))
        winsound.PlaySound('mane.wav', winsound.SND_FILENAME)

    if panda.distance(donat)<15:
        donat.goto(random.randint(-260,260),random.randint(-260,260))
        oo.goto(random.randint(-260, 260), random.randint(-260, 260))
        Score = Score +10
        wr.clear()
        wr.write('امتیاز = ' + str(Score),font=('b koodak',12,'bold'))
        winsound.PlaySound('emtiaz.wav', winsound.SND_FILENAME)

    if Score>=20:
        winsound.PlaySound('bord.wav', winsound.SND_FILENAME)
        show_winner_screen()
        winsound.PlaySound('bord.wav', winsound.SND_FILENAME)


    if Score<=-10:
        winsound.PlaySound('bakht.wav', winsound.SND_FILENAME)
        wr.goto(-75, 0)
        wr.write('،، متاسفم شما باختید :) ،، ', font=('b koodak', 18, 'bold'))

        break

turtle.mainloop()