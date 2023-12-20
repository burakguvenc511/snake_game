
import turtle
import time 
import random

oyunEkran=turtle.Screen()
oyunEkran.tracer(0)
oyunEkran.setup(600,600)
oyunEkran.bgcolor("black")

yilan = turtle.Turtle()
yilan.shape("square")
yilan.color("skyblue")
yilan.speed(0)
yilan.penup()
yilan.goto(-200,0)
yilan.yon="dur"

yem = turtle.Turtle()
yem.shape("circle")
yem.color("yellow")
yem.speed(0)
yem.penup()
yem.goto(0,0)
yem.yon="dur"

def yukari():
	if yilan.yon!="asagi":
		yilan.yon="yukari"

def asagi():
	if yilan.yon!="yukari":
		yilan.yon="asagi"

def sag():
	if yilan.yon!="sol":
		yilan.yon="sag"

def sol():
	if yilan.yon!="sag":
		yilan.yon="sol"

oyunEkran.listen()
oyunEkran.onkeypress(yukari,"w")
oyunEkran.onkeypress(asagi,"s")
oyunEkran.onkeypress(sag,"d")
oyunEkran.onkeypress(sol,"a")

oyunEkran.onkeypress(yukari,"Up")
oyunEkran.onkeypress(asagi,"Down")
oyunEkran.onkeypress(sag,"Right")
oyunEkran.onkeypress(sol,"Left")

def hareket_et():
	if yilan.yon =="yukari":
		y=yilan.ycor()
		yilan.sety(y+20)
	if yilan.yon =="asagi":
		y=yilan.ycor()
		yilan.sety(y-20)
	if yilan.yon =="sag":
		x=yilan.xcor()
		yilan.setx(x+20)
	if yilan.yon =="sol":
		x=yilan.xcor()
		yilan.setx(x-20)

bolumler=[]

while True:
	oyunEkran.update()

	if yilan.xcor()>290  or yilan.xcor()<-290 or yilan.ycor()>290  or yilan.ycor()<-290:
		time.sleep(1)
		yilan.goto(-200,0)
		yilan.yon="dur"
		for i in bolumler:
			i.goto(2000,2000)
		bolumler.clear()

	if yilan.distance(yem)<20:
		x=random.randint(-290,290)
		y=random.randint(-290,290)
		while x%20!=0 and y%20!=0:
			x=random.randint(-290,290)
			y=random.randint(-290,290)
		yem.goto(x,y)
		yenibolum=turtle.Turtle()
		yenibolum.speed(0)
		yenibolum.shape("square")
		yenibolum.penup()
		yenibolum.color("white")
		bolumler.append(yenibolum)

	for i in range(len(bolumler)-1,0,-1):
		x=bolumler[i-1].xcor()
		y=bolumler[i-1].ycor()
		bolumler[i].goto(x,y)

	if len(bolumler)>0:
		x=yilan.xcor()
		y=yilan.ycor()
		bolumler[0].goto(x,y)
	
	hareket_et()


	for i in bolumler:
		if i.distance(yilan)<20:
			time.sleep(1)
			yilan.goto(-200,0)
			yilan.yon="dur"
			for i in bolumler:
				i.goto(2000,2000)
			bolumler.clear()
			
	time.sleep(0.1)