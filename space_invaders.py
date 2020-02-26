import turtle
import math
import os
import random
import sys

# setting up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("space_invaders_background.gif")

#register shapes
turtle.register_shape("enemy.gif")
turtle.register_shape("player.gif")

# Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#SET the SCORE to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create Player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15

#Create the enemy

#multiple enemy
no_of_enemies = 5

#list of enemies
enemies = []

#Add enemies to the list
for _ in range(no_of_enemies):
    enemies.append(turtle.Turtle())

#Attributes of enemies
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
enemyspeed = 2





#create player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.15, 0.15)
bullet.hideturtle()
bulletspeed = 30

#Define bullet state
    #ready - ready to fire
    #fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declare bulletstate as a global if it needs to be changed
    global bulletstate 
    if bulletstate == "ready":
        os.system("aplay laser.wav&")
        bulletstate="fire"
        #Move the bullet to be just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



#Game run
while True:
    for enemy in enemies:
        #Move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.ycor() <-250:
            enemy.sety(-250)
            os.system("aplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            sys.exit(0)



        #Move enemy back and down

        if enemy.xcor() > 280:
            enemyspeed *= -1  #change direction

            #move down all enemies
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
        
        if enemy.xcor() <-280:
            enemyspeed *= -1    #change direction
            
            #Move down all enemies
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)

        #collision between player and enemy
        if isCollision(player, enemy):
            os.system("aplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            sys.exit(0)

        # check for collision bullet and the enemy
        if isCollision(bullet, enemy):
            os.system("aplay explosion.wav&")
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check if the bullet reached the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate = "ready"


input("Press enter to quit")