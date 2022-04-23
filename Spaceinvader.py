#Space invader using python module for android.
#That was short gameplay.
#Importing packages required.
import turtle
import random
import math


#Creating the spaceship.
sc=turtle.Screen()
sc.bgcolor("black")
sc.bgpic("Bluegalaxy.png")

score=0


#Required registrations.
turtle.register_shape("Spaceship.gif")
turtle.register_shape("Life.gif")
turtle.register_shape("Asteroid.gif")

#Creating the border.
b=turtle.Turtle()
b.speed(0)
b.color("yellow")
b.pensize(10)
b.penup()
b.pencolor("gold")
b.setposition(-530,800)
b.rt(90)
b.pendown()
b.fd(1600)
b.lt(90)
b.fd(1050)
b.lt(90)
b.fd(1600)
b.lt(90)
b.fd(1050)
b.pensize(5)
b.rt(90)
b.fd(101)
b.rt(90)
b.fd(1050)
b.rt(90)
b.fd(96)
b.hideturtle()

#Creating game score.
sr=turtle.Turtle()
sr.color("gold")
sr.shape("square")
sr.penup()
sr.hideturtle()
sr.goto(-520,820)
scorestring = "Score: %s" %score
sr.write(scorestring, False, align="left", font=("Arial", 11, "normal"))
sr.hideturtle()

#Creating game life.
a_axis=[320,390,460]
b_axis=[850]
for i in a_axis:
	for j in b_axis:
		 l=turtle.Turtle()
		 l.shape("Life.gif")
		 l.penup()
		 l.goto(i,j)

		 
#Creating the spaceship.
p=turtle.Turtle()
p.shape("Spaceship.gif")
p.penup()
p.speed(0)
p.goto(0,-700)
p.setheading(90)

pspeed=50

#Creating the bullet.
blt=turtle.Turtle()
blt.shape("arrow")
blt.shapesize(1,10)
blt.color("yellow")
blt.penup()
blt.speed(0)
blt.setheading(90)
blt.hideturtle()

bltspeed=190

bltstate="ready"


#Creating enemy.
num_of_enemies=20
enemies=[]
for i in range(num_of_enemies):
	enemies.append(turtle.Turtle())
for e in enemies:	
	e.shape("Asteroid.gif")
	e.penup()
	e.speed(0)
	x=random.randint(-495,400)
	y=random.randint(300,765)
	e.setposition(x,y)
	

espeed=5

#Functions to move player.
def moveleft():
	x=p.xcor()
	x-=pspeed
	if x<-400:
		x=-400
	p.setx(x)
	
def moveright():
	x=p.xcor()
	x+=pspeed
	if x>390:
		x=390
	p.setx(x)
	
def fireblt():
	global bltstate
	if bltstate=="ready":
		bltstate="fire"
		x=p.xcor()
		y=p.ycor()+31
		blt.setposition(x,y)
		blt.showturtle()
		
def iscollision(t1,t2):
		distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
		if distance < 85:
				return True
		else:
				return False
				
#Keyboard bindings.
sc.listen()
sc.onkeypress(moveleft,"Left")
sc.onkeypress(moveright,"Right")
sc.onkeypress(fireblt,"space")
while True:
	for e in enemies:
		x=e.xcor()
		x+=espeed
		e.setx(x)
		
		if x<-495:
			y=e.ycor()
			y-=100
			espeed*=-1
			e.sety(y)
			
		if x>488:
			y=e.ycor()
			y-=100
			espeed*=-1
			e.sety(y)
			
		if iscollision(blt,e):
			blt.hideturtle()
			bltstate="ready"
			blt.setposition(0,-2300)
			x=random.randint(-495,350)
			y=random.randint(350,765)
			e.setposition(x,y)
			score+=10
			sr.clear()
			sr.write(scorestring, False, align="left", font=("Arial", 11, "normal"))

			scorestring="Score:%s"%score			
		a_axis=[320,390,460]
		b_axis=[850]
		for i in a_axis:
			for j in b_axis:
				 if iscollision(e,l):
				 	i=i-1
	
			
		if iscollision(p,e):
			p.hideturtle()
			e.hideturtle()
			print("Game Over")
			break
			
	y=blt.ycor()
	y+=bltspeed
	blt.sety(y)
	
	if blt.ycor()>535:
		blt.hideturtle()
		bltstate="ready"
	
#Thanks a lot for watching.	

	

