import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.listen()




player = Player()
scores = Scoreboard()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
lanes = [-230, -200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100, 130, 160, 190, 220]
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.move, "w")
def pause_game():
        global game_paused
        game_paused = not game_paused
all_car = []
game_paused = False

screen.onkeypress(pause_game, "p")
game_is_on = True
while game_is_on:
    time.sleep(scores.car_speed)
    screen.update()
        
    if not game_paused:
       

        
        new_car = CarManager()
        y_random = random.randint(-230, 230 )
        new_car.color(random.choice(COLORS))
        new_car.goto(x=520, y=random.choice(lanes))

        if game_paused:
            scores.goto(0,0)
            scores.write("PAUSED", align="center", font=("Arial",30,"bold"))
        else:
            scores.clear()
            scores.update_scoreboard()
            scores.update_lives()
        
        if player.ycor() > 290:
            player.reset_position()
            scores.increase_score()

        if random.randint(0, 6) == 3 or random.randint(0, 5) == 1:
            new_car
            all_car.append(new_car)

        for car in all_car:
            new_x = car.xcor() - 20
            new_y = car.ycor()
            car.goto(new_x, new_y)

            if player.distance(car) < 20:
                scores.live()
                player.reset_position()
            if scores.lives <= 0:
                scores.game_over()
                game_is_on = False

    if game_paused:
        scores.goto(0,0)
        scores.write("PAUSED", align="center", font=("Arial",30,"bold"))   
        print(scores.car_speed)  
screen.exitonclick()