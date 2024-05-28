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
            deleteSprite(projectile)
            continue
        projectile.setx(x)
        projectile.sety(y)

def deleteSprite(sprite):
    sprite.hideturtle()
    # Try and remove the sprite from both lists
    # This method sucks but the real solution is long and complicated
    try:
        enemy_list.remove(sprite)
    except:
        try:
            projectile_list.remove(sprite)
        except:
            pass # ew, bad, kill it with fire !!! (sorry)

def spriteCollide(spriteName1, spriteName2, diameter=100):
    spriteName1 = spriteName1.lower()
    spriteName2 = spriteName2.lower()
    if spriteName1 == spriteName2:
        print("A sprite cannot collide with itself")
        print("===================================")
        return None, None
    if not (spriteName1 == "player" or spriteName1 == "enemy" or spriteName1 == "projectile"):
        print("The FIRST sprite name does not match any existing sprite (player, enemy, projectile)")
        print("====================================================================================")
        return None, None
    if not (spriteName2 == "player" or spriteName2 == "enemy" or spriteName2 == "projectile"):
        print("The SECOND sprite name does not match any existing sprite (player, enemy, projectile)")
        print("=====================================================================================")
        return None, None

    # Set up the turtles to always be arrays based on the different types
    turtle1 = None
    turtle2 = None
    if spriteName1 == "player":
        turtle1 = [ player ]
    if spriteName2 == "player":
        turtle2 = [ player ]
    if spriteName1 == "enemy":
        turtle1 = enemy_list
    if spriteName2 == "enemy":
        turtle2 = enemy_list
    if spriteName1 == "projectile":
        turtle1 = projectile_list
    if spriteName2 == "projectile":
        turtle2 = projectile_list


    for t1 in turtle1:
        for t2 in turtle2:
            # a^2 + b^2 <= c^2 --> sqrt(a^2 + b^2) <= c
            if (t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2 <= diameter**2:
                return t1, t2   # Return which sprites collided
    return None, None













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
playing_game = True
while playing_game:
    enemyCreateTimer = enemyCreateTimer + 1
    if enemyCreateTimer >= 100:
        enemy_x = random.randrange(-screenWidth, screenWidth)
        enemy_y = screenHeight
        addEnemy(enemy_x, enemy_y)
        enemyCreateTimer = 0

    xspeed = 0
    yspeed = 100
    moveProjectiles(xspeed, yspeed)
    projectile_sprite, enemy_sprite = spriteCollide("projectile", "enemy")
    if projectile_sprite and enemy_sprite:
        deleteSprite(enemy_sprite)
        deleteSprite(projectile_sprite)

    player_sprite, enemy_sprite = spriteCollide("player", "enemy")
    if player_sprite and enemy_sprite:
        print("====================================================================================")
        print("                                Game Over")
        print("====================================================================================")
        playing_game = False

    screen.update()
