from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
lanes = [-230, -200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100, 130, 160, 190, 220]
random_color = random.choice(COLORS)
y_random = random.randint(-230, 230 )

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random_color)
        self.penup()
        self.forward(20)
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)    
        
        self.goto(x=500, y=random.choice(lanes))
        

    def move(self):
        new_x = self.xcor() - 20
        new_y = self.ycor()
        self.goto(new_x, new_y)

    
        

  
    
    # def reset_position(self):
    #     self.goto(x=480, y=-120)