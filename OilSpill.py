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
screenWidth = 1024//2
screenHeight = 760//2
screen = turtle.Screen()
screen.setup(width=screenWidth*2, height=screenHeight*2)
screenWidth -= 50   # Adjust for sprite sizes to help with wall collision centering
screen.title("Oil Spill Clean Up")
screen.bgcolor("black")
screen.bgpic(backgroundImage)


# Create the player
player = turtle.Turtle()
player.shape(playerImage)
player.penup()
player.speed(0)
player.setposition(0, -screenHeight/2)

# Create the enemies
global enemy_list_index, enemy_list_len
enemy_list_index = 0
enemy_list_len = 4
enemy_list = []
enemy_vx_direction_list = []    # 1 for normal movement, -1 for reverse movement after wall bounce
for i in range(enemy_list_len):
    enemy = turtle.Turtle()
    enemy.penup()
    enemy.hideturtle()
    enemy.shape(enemyImage)
    enemy_list.append(enemy)
    enemy_vx_direction_list.append(1)

def addEnemy(x, y):
    global enemy_list_index, enemy_list_len
    if enemy_list_index >= enemy_list_len:
        return
    enemy_list[enemy_list_index].setposition(x, y)
    enemy_list[enemy_list_index].showturtle()
    enemy_list_index += 1

def moveEnemies(vx, vy, bounce_on_walls=False):
    for i in range(len(enemy_list)):
        x = enemy_list[i].xcor() + vx*enemy_vx_direction_list[i]
        y = enemy_list[i].ycor() + vy
        if bounce_on_walls and (x <= -screenWidth or x >= screenWidth):
            enemy_vx_direction_list[i] *= -1
        enemy_list[i].setx(x)
        enemy_list[i].sety(y)


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

def moveProjectiles(vx=0, vy=100, bounce_on_walls=False):
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

    def getSpriteList(name):
        if name == "player":
            return [player]
        elif name == "enemy":
            return enemy_list
        elif name == "projectile":
            return projectile_list
        print("One of the sprite name do not match any existing sprite (player, enemy, projectile)")
        print("====================================================================================")
        return []

    sprite1 = getSpriteList(spriteName1)
    sprite2 = getSpriteList(spriteName2)

    for s1 in sprite1:
        for s2 in sprite2:
            if (s1.xcor() - s2.xcor())**2 + (s1.ycor() - s2.ycor())**2 <= diameter**2:
                return s1, s2
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
    # Creating enemies on a timer
    enemyCreateTimer = enemyCreateTimer + 1
    if enemyCreateTimer >= 2:
        enemy_x = random.randrange(-screenWidth, screenWidth)
        enemy_y = screenHeight
        addEnemy(enemy_x, enemy_y)
        enemyCreateTimer = 0

    # Moving the projectiles and the enemies
    xspeed = 0
    yspeed = 100
    moveProjectiles(xspeed, yspeed)
    xspeed = 60
    yspeed = -20
    bounce_on_walls = True
    moveEnemies(xspeed, yspeed, bounce_on_walls)

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
