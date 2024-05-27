import turtle
import random

imageDirectory = "files/images/"
playerImage = imageDirectory+"player.gif"
enemyImage = imageDirectory+"enemy.gif"
projectileImage = imageDirectory+"projectile.gif"
backgroundImage = imageDirectory+"background.gif"
# For some reason png's do not work


# Register the shapes
turtle.register_shape(playerImage)
turtle.register_shape(enemyImage)
turtle.register_shape(projectileImage)

# Initialize the screen
screenWidth = 1280//2
screenHeight = 960//2
screen = turtle.Screen()
screen.setup(width=screenWidth*2, height=screenHeight*2)
screen.title("Oil Spill Clean Up")
screen.bgcolor("black")
screen.bgpic("files/images/background.gif")


# Create the player
player = turtle.Turtle()
player.shape(playerImage)
player.penup()
player.speed(0)
player.setposition(0, -screenHeight/2)

# Create the enemies
enemy_list = []
def addEnemy(x, y):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.penup()
    enemy.setposition(x, y)
    enemy.shape(enemyImage)
    enemy_list.append(enemy)

# Create the projectiles
projectile_list = []
def addProjectile():
    projectile = turtle.Turtle()
    projectile.speed(0)
    projectile.penup()
    x = player.xcor()
    y = player.ycor()
    projectile.setposition(x, y)
    projectile.shape(projectileImage)
    projectile_list.append(projectile)

def moveProjectiles(vx=0, vy=100):
    for projectile in projectile_list:
        x = projectile.xcor() + vx
        y = projectile.ycor() + vy
        if x < -screenWidth or x > screenWidth or y < -screenHeight or y > screenHeight:
            deleteProjectile(projectile)
            continue
        projectile.setx(x)
        projectile.sety(y)

def deleteProjectile(projectile):
    projectile.hideturtle()
    projectile_list.remove(projectile)

def spriteCollide(s1, s2, diameter=100):
    # a^2 + b^2 >= c^2 --> sqrt(a^2 + b^2) >= c
    return (s1.xcor()-s2.xcor())**2 + (s1.ycor()-s2.ycor())**2 >= diameter**2

# Define functions to control player movement
def move_left():
    x = player.xcor()
    x = x - 50
    if not x < -screenWidth:
        player.setx(x)

def move_right():
    x = player.xcor()
    x = x + 50
    if not x > screenWidth:
        player.setx(x)

def shoot_projectile():
    addProjectile()

# Set up keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
turtle.onkey(shoot_projectile, "space")

# Main game loop
enemyCreateTimer = 0
while True:
    enemyCreateTimer = enemyCreateTimer + 1
    if enemyCreateTimer >= 100:
        enemy_x = random.randrange(-screenWidth, screenWidth)
        enemy_y = screenHeight
        addEnemy(enemy_x, enemy_y)
        enemyCreateTimer = 0

    moveProjectiles(0, 100)
    screen.update()
