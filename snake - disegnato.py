#!/usr/bin/python3
#made with love by Eduzyolo on github
import turtle
import time
import random
from threading import Timer

#################################################################################################################################################################

#varibles
delay = 0.1
SIZE = 10
gss = {#game screen size
    "x_DX": 80,
    "y_DX": -15,
    "x_SX": 340,
    "y_SX": 245,
    "x_CE": 0,
    "y_CE": 0
}
gss["x_CE"] , gss["y_CE"] = (gss["x_SX"]+gss["x_DX"])/2,(gss["y_DX"]+gss["y_SX"])/2
score = 0# used for save the score during the game
top_player = []# save the name and score of all the player

# Snake head
head = turtle.Turtle()
head.shape("circle")
head.speed(0)
head.resizemode("user")
head.shapesize(SIZE/20, SIZE/20, 1)
head.color("#CC0066")
head.penup()
head.goto(gss["x_CE"],gss["y_CE"])
head.direction = "stop"
head.hideturtle()

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.shapesize(SIZE/20, SIZE/20, 1)
food.color("blue")
food.penup()
food.goto(gss["x_CE"],gss["y_CE"]+(SIZE*3))
food.hideturtle()

#queue of the snake
segments = []
wn = turtle.Screen()
wn.setup(800,600,0,0)
wn.title("Snake Game")
wn.tracer(0)

#pen used for draw all the background
pen = turtle.Turtle()
pythonsize=3
pen.pensize(pythonsize)
pen.speed(10)
pen.seth(90)

#pen used for draw the ranking
pen_cla = turtle.Turtle()
pythonsize=3
pen_cla.pensize(pythonsize)
pen_cla.speed(10)
pen_cla.seth(90)
pen_cla.hideturtle()

#pen used for color the buttons
pen_btn = turtle.Turtle()
pythonsize=3
pen_btn.pensize(pythonsize)
pen_btn.speed(10)
pen_btn.seth(90)

#pen used for sccore
pen_score = turtle.Turtle()
pythonsize=3
pen_score.pensize(pythonsize)
pen_score.speed(10)
pen_score.seth(90)
#################################################################################################################################################################

# Functions

def color_btn(x,y,color):
    pen_btn.penup()  
    pen_btn.goto(x,y)
    pen_btn.pendown()
    pen_btn.begin_fill()
    pen_btn.color(color)
    round_rectangle(70,30,90,2,pen_btn)
    pen_btn.end_fill()
    wn.ontimer(normal_btn, 250)

def normal_btn():
    x,y= 340,-210
    for i in range(3):
        for j in range(3):
            pen_btn.penup()  
            pen_btn.goto(x,y)
            pen_btn.pendown()
            pen_btn.begin_fill()
            pen_btn.color("#3c3c3c")
            round_rectangle(70,30,90,2,pen_btn)
            pen_btn.end_fill()
            x=x-(71+24)
        y=y+50
        x=340
    
def go_up():
    if head.direction != "down":
        head.direction = "up"
        color_btn(245,-110,"#00FF00")
        
def go_down():
    if head.direction != "up":
        head.direction = "down"
        color_btn(245,-210,"#0000FF")

def go_left():
    if head.direction != "right":
        head.direction = "left"
        color_btn(150,-160,"#FF0000")

def go_right():
    if head.direction != "left":
        head.direction = "right"
        color_btn(340,-160,"#FFFF00")

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + SIZE)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - SIZE)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - SIZE)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + SIZE)

def restart_game():
    global score
    global segments
    global wn
    global top_player
    
    head.goto(gss["x_CE"],gss["y_CE"])
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
        
    # Clear the segments list
    segments.clear()
    player = {"name":None,"points":0}
    while player["name"]==None or player["name"]=="" or len(player["name"])>25:
        player["name"] = wn.textinput("Name", "Please enter your name\n(MAX caracter 25): ")
    player["points"] = score
    top_player.append(player)

    score = 0
    top_player = sorted(top_player, key=lambda x : x['points'], reverse=True)
    pen_cla.clear()
    pen_cla.penup()
    pen_cla.goto(-360,210)
    pen_cla.pendown()
    pen_cla.write("RANKING\n\r",align="left",font=("Lucida Sans",16,"normal"))
    s_length = 41
    i=1
    for pla in top_player[0:16]:
        pen_cla.penup()
        pen_cla.goto(-360,210-(i*27))
        pen_cla.pendown()
        pen_cla.write(pla["name"],align="left")
        pen_cla.penup()
        pen_cla.goto(-160,210-(i*27))
        pen_cla.pendown()
        pen_cla.write(str(pla["points"]),align="left")
        i=i+1

    pen_cla.hideturtle()
    pen_score.clear()
    # Reset the delay
    global delay
    delay = 0.1
    print("i'm ready")
    
def round_rectangle(length,high,cor_angle,cor_rad,the_pen=pen):    
    for i in range(2):
        the_pen.fd(high)
        the_pen.circle(cor_rad,cor_angle)
        the_pen.fd(length)
        the_pen.circle(cor_rad,cor_angle)      



def draw_game():    
    #draw the ranking rectangle and color it
    pen.penup()  
    pen.goto(-80,-240)#from x remove 30 from y remove 60
    pen.pendown()
    pen.begin_fill()
    pen.color("#F0F0F0")
    round_rectangle(275,495,90,15)
    pen.end_fill()
    
    #draw the game rectangle and color it
    pen.penup()  
    pen.goto(370,-240)#from x remove 30 from y remove 60
    pen.pendown()
    pen.begin_fill()
    pen.color("#F0F0F0")
    round_rectangle(260,480,90,30)
    pen.end_fill()

    #draw the border of the game rectangle
    pen.pencolor("#8E8e8e")
    pen.penup()  
    pen.goto(370,-240)
    pen.pendown()
    round_rectangle(260,480,90,30)

    #draw the game screen
    pen.pencolor("black")
    pen.penup()  
    pen.goto(340,-15)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    round_rectangle(260,260,90,0)
    pen.end_fill()

    #draw the buttons
    normal_btn()
    
    pen.pendown()
    pen.hideturtle()
    pen_btn.hideturtle()
    pen_score.hideturtle()
    global head
    global food
    head.showturtle()
    food.showturtle()
    print("x game lenght: "+str(gss["x_CE"]-gss["x_DX"])+"; y game lenght: "+str(gss["y_CE"]-gss["y_DX"]))


#################################################################################################################################################################

#game
draw_game()


# Keyboard bindings
wn.listen()
#nerd command
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
#normal people command
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.listen()
    wn.update()
    # Check for a collision with the border
    #print(str(head.ycor())+";"+str(gss["y_DX"]+SIZE)+";"+str((gss["y_SX"]+SIZE)))
    if head.xcor()>gss["x_SX"]-(SIZE/2) or head.xcor()<gss["x_DX"]+(SIZE/2) or head.ycor()>gss["y_SX"]-(SIZE/2) or head.ycor()<gss["y_DX"]+(SIZE/2):
        print("collision HEAD BORDER:\tGAME OVER") 
        restart_game()

    # Check for a collision with the food
    if head.distance(food) < SIZE:
        print("collision HEAD FOOD")
        uncorret_random = True
        #segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.shapesize(SIZE/20, SIZE/20, 1)
        new_segment.color("#FF3333")
        new_segment.penup()

        segments.append(new_segment)
        i=0
        # da sistyemare uscita dal ciclio while
        while uncorret_random:
            # Move the food to a random spot
            #print((random.randint(int((gss["x_CE"]-gss["x_SX"])/SIZE), int((gss["x_CE"]-gss["x_DX"])/SIZE)))
            x = (random.randint(int((gss["x_CE"]-gss["x_SX"])/SIZE), int((gss["x_CE"]-gss["x_DX"])/SIZE))*SIZE)+gss["x_CE"]
            #x = (random.randint(0, int((gss["x_CE"]-gss["x_DX"])/SIZE))*SIZE)-gss["x_CE"]
            #-SIZE,SIZE)*SIZE-(gss["x_CE"])#-gss["x_DX"])#(random.randint(gss["x_CE"],gss["x_SX"])%SIZE)#*SIZE-gss["x_CE"]
            y = (random.randint(int((gss["y_CE"]-gss["y_SX"])/SIZE), int((gss["y_CE"]-gss["y_DX"])/SIZE))*SIZE)+gss["y_CE"]
            #-SIZE,SIZE)*SIZE-(gss["y_CE"])#-gss["y_DX"])#(random.randint(gss["y_DX"],gss["y_SX"])*SIZE)#*SIZE-gss["y_CE"]
            for segment in segments:
                if segment.xcor()== x and segment.ycor()== y:
                    print("FOOD is in SEGMENT")
                    i=i+1
                    uncorret_random = True
                    time.sleep(0.002)
                    break #stop the for cicle othervise the shile cicle will terminate with the if write after this line
                if segment.xcor()!= x or segment.ycor()!= y:
                    uncorret_random = False
            if(x>gss["x_SX"]-(SIZE/2)or x<gss["x_DX"]+(SIZE/2) or y>gss["y_SX"]-(SIZE/2)or y<gss["y_DX"]+(SIZE/2)):
                    print("FOOD is OUT of GAME screen")
                    i=i+1
                    uncorret_random = True
                    time.sleep(0.002)
        print("x:"+str(x)+";y:"+str(y)+";i:"+str(i))
        
        food.goto(x,y)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        pen_score.clear()
        pen_score.penup()
        pen_score.goto(195,-60)
        pen_score.pendown()
        pen_score.write(str(score),align="left",font=("Lucida Sans",14,"normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < SIZE:
            print("collision HEAD BODY:\tGAME OVER")
            restart_game()

    time.sleep(delay)

wn.mainloop()




'''
    turtle.penup()  
    turtle.goto(0,265)-
    pendown()
    turtle.begin_fill()
    turtle.color("#3c3c3c")
    turtle.circle(6,360)
    turtle.end_fill()

    turtle.pencolor("#9d9d9d")
    turtle.penup()  
    turtle.goto(75,-185)
    turtle.pendown()
    turtle.circle(25,360)
    turtle.penup()  
    turtle.goto(80,265)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#9d9d9d")
    round_rectangle(60,4,90,1)
    turtle.end_fill()
    
    turtle.pencolor("#8E8e8e")
    turtle.penup()  
    turtle.goto(370,-240)#from x remove 30 from y remove 60
    turtle.pendown()
    round_rectangle(267,484,90,30)'''
