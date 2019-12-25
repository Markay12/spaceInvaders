#Space Invaders - Part 1
#import main files
import turtle
import os

#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#draw the border 

border_pen = turtle.Turtle() #create turtle to draw
border_pen.speed(0) #set speed of drawing(0 is the quickest)
border_pen.color("white")
border_pen.penup() #keeps pen off the ground
border_pen.setposition(-300, -300)
border_pen.pensize(3)
border_pen.pendown()

for side in range(4): # go through all four corners
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle() # so we don't see the turtle draw


# create enemies
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250) # add at top left


#Create the player's bullet (defense)

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed()
bullet.setheading(90)
bullet.shapesize(0.33, 0.33)
bullet.hideturtle()

# define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready" #when game starts


# create the player turtle
player1 = turtle.Turtle()
player1.color("blue")
player1.shape("triangle")
player1.penup()
player1.speed(0)
player1.setposition(0, -250) # center x and towards the bottom at -300
player1.setheading(90) #player starts facing fowards




# move the player same as event keys in java
playerspeed = 14  #how far we want the user to move when selecting a control
enemyspeed = 2
bulletspeed = 20

#functions to move player left right and bind to key
def move_left():
    x = player1.xcor() # gets the player position
    x -= playerspeed

    if x < -280: #sets left boundary
        x = -280

    player1.setx(x) #updated player x position

def move_right():
    x = player1.xcor() # gets the player position
    x += playerspeed

    if x > 280: #sets right boundary
        x = 280

    player1.setx(x) # updated player position

def fire_bullet():
    #Declare bulletstate as global
    global bulletstate # create global variable within a function

    if bulletstate == "ready":
        
        bulletstate = "fire"  

        # Move bullet to player to look like shooting
        x = player1.xcor()
        y = player1.ycor() + 15
        bullet.setposition(x, y)
        bullet.showturtle()
    


# create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



# create main game loop (while)

while True:

    #move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #move the enemy back and down

    if enemy.xcor() > 282:
        y = enemy.ycor()
        enemy.speed(1)
        y -= 40
        enemy.sety(y)
        enemy.speed(0)
        enemyspeed *= -1

    if enemy.xcor() < -282:
        y = enemy.ycor()
        y -= 40
        enemy.speed(1)
        enemy.sety(y)
        enemy.speed(0)
        enemyspeed *= -1

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # check bullet boundaries

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



# set delay so the window stays open
delay = input("Press ENTER to exit.")