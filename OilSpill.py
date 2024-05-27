import turtle

imageDirectory = "files/images/"
playerImage = imageDirectory+"player.gif"
enemyImage = imageDirectory+"enemy.gif"
backgroundImage = imageDirectory+"background.gif"
# Register the shapes (for some reason png does not work)
turtle.register_shape(playerImage)
turtle.register_shape(enemyImage)

# Initialize the screen
screen = turtle.Screen()
screen.setup(width=1080, height=720)
screen.title("Oil Spill Clean Up")
screen.bgcolor("black")
screen.bgpic(backgroundImage)


# Create the player
player = turtle.Turtle()
player.shape(playerImage)
player.penup()
player.speed(0)

# Create the enemies
enemyList = []
def addEnemy(x, y):
    enemy = turtle.Turtle()
    enemy.shape(enemyImage)
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(x, y)
    enemyList.append(enemy)

# Define functions to control player movement
def move_left():
    x = player.xcor()
    x -= 10
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 10
    player.setx(x)

# Set up keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()
