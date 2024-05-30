import turtle
import math
import random

#Set up the screen
set = turtle.Screen()
set.bgcolor("dark blue")
set.title("Oil Spill Clean Up")
set.bgpic("River.gif")
set.setup(width=1024, height=760)

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-400, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, font=("Arial", 20))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


#Choose a number of blobs
number_of_blobs = 5
#Create an empty list of blobs
blobs = []

#Add blobs to the list
for i in range(number_of_blobs):
	#Create the oil
	blobs.append(turtle.Turtle())

for oil in blobs:
	oil.color("red")
	oil.shape("invader.gif")
	oil.penup()
	oil.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	oil.setposition(x, y)

oilspeed = 5


#Create the player's cleaner
cleaner = turtle.Turtle()
cleaner.color("white")
cleaner.shape("triangle")
cleaner.penup()
cleaner.speed(0)
cleaner.setheading(90)
cleaner.shapesize(1, 1)
cleaner.hideturtle()

cleanerspeed = 40

#================================================================================================================================================
#================================================================================================================================================
#================================================================================================================================================
#================================================================================================================================================
#================================================================================================================================================
#================================================================================================================================================


#Move the player left and right

#Create keyboard bindings

cleanerstate = "ready"

def clean_up():
	global cleanerstate
	if cleanerstate == "ready":
		cleanerstate = "gone"
		x = player.xcor()
		y = player.ycor() + 10
		cleaner.setposition(x, y)
		cleaner.showturtle()

def Collision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

#Create keyboard bindings 2
turtle.listen()
turtle.onkey(clean_up, "space")

#Main game loop
while True:

	for oil in blobs:
		#Move the oil
		x = oil.xcor()
		x += oilspeed
		oil.setx(x)

		#Move the oil back and down
		if oil.xcor() > 280:
			#Move all blobs down
			for e in blobs:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change oil direction
			oilspeed *= -1.2

		if oil.xcor() < -280:
			#Move all blobs down
			for e in blobs:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change oil direction
			oilspeed *= -1.2

		#Check for a collision between the cleaner and the oil

			# Create score


		#Check for a collision between the player and the oil





	#Move the cleaner
	if cleanerstate == "gone":
		y = cleaner.ycor()
		y += cleanerspeed
		cleaner.sety(y)

	#Check to see if the cleaner has gone to the top
	if cleaner.ycor() > 275:
		cleaner.hideturtle()
		cleanerstate = "ready"


delay = raw_input("Press enter to finsh.")
