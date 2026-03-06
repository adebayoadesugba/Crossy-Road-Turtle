from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("Black")
        self.penup()
        self.hideturtle()
        
        self.car_speed = 0.15
        self.update_scoreboard()
        self.update_lives()
        

    def update_scoreboard(self):
        self.goto(x=-420, y=250)
        self.write(f"Level: {self.score}", align="center", font=("Arial", 20, "normal"))

    def update_lives(self):
        self.goto(x=420, y=250)
        self.write(f"LIVES: {self.lives}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.car_speed *= 0.7
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.update_lives()
   
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Arial", 32, "normal"))

    def live(self):
        
        self.lives -= 1
        self.clear()
        self.update_lives()
        self.update_scoreboard()

   
