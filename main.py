import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Cars
from scoreboard import Scoreboard

CONST_WIDTH = 600
CONST_HEIGHT = 600

screen = Screen()
screen.setup(width=CONST_WIDTH, height=CONST_HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")
# screen.onkey(player.move_down, "d") # only move up


game_is_on = True
listOfCars = []
counter = 0
round = 0
speedIncrease = 0
# screen_refresh_rate = 0.1
while game_is_on:
    time.sleep(0.02)
    screen.update()

    if (counter % 25 == 0):  # generate a new car every 0.6 seconds
        c = Cars()
        c.increaseSpeed(speedIncrease)
        listOfCars.append(c)  # add the new car to the list

    # iterate through each car
    for car in listOfCars:

        # check for collision with cars
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

        # check if car is out of screen
        if car.ycor() > CONST_WIDTH / 2:
            car.hideturtle()
            listOfCars.remove(car)  # remove from list

        car.move()  # move car

    # check if player has won
    if (player.ycor() > (250)):
        print("you've won!")
        round += 1
        speedIncrease += 0.5  # increase Car speed
        counter = 0
        player.reset_location()
        scoreboard.increase_score()

        for car in listOfCars:
            car.hideturtle()  # hide the cars

        listOfCars = []  # clear list of cars

    counter += 1

screen.exitonclick()