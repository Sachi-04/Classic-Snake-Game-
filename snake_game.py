from turtle import Turtle , Screen, xcor, ycor
import time
import random

# --- Constants ---
# Directional headings in degrees
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Game configuration
MOVE_DISTANCE=20
colors=["red","light blue","yellow","light green","pink","orange","violet"]
font="Courier",15,"bold"
screen= Screen()
screen.title("The snake game..")
starting_position=[(0,0), (-20,0), (-40,0)]


is_on=True

# --- Classes ---

class Scoreboard(Turtle):
    # Handles the display of the score and Game Over text
    def __init__(self) :
        super().__init__()
        self.score=0
        self.goto(0,270)            # Position at the top of the screen
        self.color("white")
        self.write(f"Score: {self.score}",move=False,align="center",font=(font))           #shows current score
        self.hideturtle()      # hide_turtle() is used because we only want to see text, not the turtle icon
    
    def game_over(self):
        # Displays 'GAME OVER' at the center of the screen.
        self.goto(0,0)
        self.write(f"GAME OVER",move=False,align="center",font=(font))
            
    # Increments score, clears previous text, and updates display
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",move=False,align="center",font=(font))

        

class Snake:
    #Handles snake creation, movement, and direction control
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]    # The first segment is the head

    def create_snake(self):
        # Initializes the snake body based on starting positions
        for position in starting_position:
            self.add_segment(position) 

    def add_segment(self,position):
        # Creates a new square turtle segment and adds it to the list.
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment) 

    def extend(self):
        # Adds a new segment to the snake at the tail's current position.
        self.add_segment(self.segments[-1].position())


    def move(self):
        """
        Moves the snake forwards.
        Logic: Starting from the tail, move each segment to the position 
        of the segment immediately in front of it. Finally, move the head forward.
        """
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

              # --- Direction Control Methods ---
    # These methods check the current heading to prevent the snake 
    # from reversing directly into itself (e.g., going Down while moving Up).

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

class Food(Turtle):
    # Handles the food object appearance and relocation.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # Resize the turtle shape to be smaller than the snake (10x10 size)
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(random.choice(colors))
        self.speed("fast")
        # self.speed("fast")   
       
    def refresh(self):
        self.color(random.choice(colors))
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)

        
food=Food()
snake=Snake()
screen.listen()
score=Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The snake game..")    
screen.tracer(0)

while is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>298 or snake.head.xcor()<-298 or snake.head.ycor()>298 or snake.head.ycor()<-298: 
        is_on=False
        score.game_over()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            is_on=False
            score.game_over()


        







screen.exitonclick()