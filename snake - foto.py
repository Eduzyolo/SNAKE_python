import turtle
import time
import random 

# center x game = -5
# center y game = 185
# angle down SX: -150,76
# angle down DX: 140,76
# angle up SX: -150,294
# angle up DX: 140,294

#varibles
delay = 0.1
SIZE = 10
gss = {#game screen size
    "x_DX": -150,
    "y_DX": 76,
    "x_SX": 140,
    "y_SX": 294,
    "x_CE": 0,
    "y_CE": 0
    }

gss["x_CE"] , gss["y_CE"] = (gss["x_SX"]+gss["x_DX"])/2,(gss["y_DX"]+gss["y_SX"])/2
score = 0
top_score = []

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgpic("Snake8.gif")
wn.bgcolor("#99FFFF")
wn.setup(width=480, height=599)#image dimensions
wn.tracer(0) # Turns off the screen updates

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

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.shapesize(SIZE/20, SIZE/20, 1)
food.color("blue")
food.penup()
food.goto(gss["x_CE"],gss["y_CE"]+(SIZE*3))

#queue of the snake
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 50)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 10, "normal"))

print("x game lenght: "+str(gss["x_CE"]-gss["x_DX"])+"; y game lenght: "+str(gss["y_CE"]-gss["y_DX"]))
print(wn.getshapes())
for i in range(0,10):
    x = (random.randint(int((gss["x_CE"]-gss["x_SX"])/SIZE), int((gss["x_CE"]-gss["x_DX"])/SIZE))*SIZE)-gss["x_CE"]
            #-SIZE,SIZE)*SIZE-(gss["x_CE"])#-gss["x_DX"])#(random.randint(gss["x_CE"],gss["x_SX"])%SIZE)#*SIZE-gss["x_CE"]
    y = (random.randint(int((gss["y_CE"]-gss["y_SX"])/SIZE), int((gss["y_CE"]-gss["y_DX"])/SIZE))*SIZE)+gss["y_CE"]
    time.sleep(0.002)
    print("x:"+str(x)+";y:"+str(y))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

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
    head.goto(gss["x_CE"],gss["y_CE"])
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
        
    # Clear the segments list
    segments.clear()
    global score
    if score > top_score[0]:
        top_score[0] = score
    # Reset the score
    score =0

    # Reset the delay
    global delay
    delay = 0.1
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, top_score[0][1]), align="center", font=("Courier", 10, "normal"))


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
    wn.update()

    # Check for a collision with the border
    #print(str(head.ycor())+";"+str(gss["y_DX"]+SIZE)+";"+str((gss["y_SX"]+SIZE)))
    if head.xcor()>gss["x_SX"] or head.xcor()<gss["x_DX"] or head.ycor()>gss["y_SX"] or head.ycor()<gss["y_DX"]:
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
            x = (random.randint(int((gss["x_CE"]-gss["x_SX"])/SIZE), int((gss["x_CE"]-gss["x_DX"])/SIZE))*SIZE)-gss["x_CE"]
            #x = (random.randint(0, int((gss["x_CE"]-gss["x_DX"])/SIZE))*SIZE)-gss["x_CE"]
            #-SIZE,SIZE)*SIZE-(gss["x_CE"])#-gss["x_DX"])#(random.randint(gss["x_CE"],gss["x_SX"])%SIZE)#*SIZE-gss["x_CE"]
            y = (random.randint(int((gss["y_CE"]-gss["y_SX"])/SIZE), int((gss["y_CE"]-gss["y_DX"])/SIZE))*SIZE)+gss["y_CE"]
            #-SIZE,SIZE)*SIZE-(gss["y_CE"])#-gss["y_DX"])#(random.randint(gss["y_DX"],gss["y_SX"])*SIZE)#*SIZE-gss["y_CE"]
            for segment in segments:
                if segment.xcor()== x and segment.ycor()== y:
                    print("FOOD is in SEGMENT")
                    i=i+1
                    uncorret_random = True
                    break #stop the for cicle othervise the shile cicle will terminate with the if write after this line
                if segment.xcor()!= x or segment.ycor()!= y:
                    uncorret_random = False
            if(x>gss["x_SX"]or x<gss["x_DX"] or y>gss["y_SX"]or y<gss["y_DX"]):
                    print("FOOD is OUT of GAME screen")
                    i=i+1
                    uncorret_random = True
        print("x:"+str(x)+";y:"+str(y)+";i:"+str(i))
        time.sleep(0.002)
        food.goto(x,y)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, top_score[0]), align="center", font=("Courier", 10, "normal")) 

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
