import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()

car = CarManager()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    # refresh the screen (everything inside this while-loop) every 0.1 second
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move_player, 'Up')
    car.create_car()
    car.move_car()
    scoreboard.show_level()

    # 'cars' is a list, from 'car_manager' file
    for c in car.cars:
        # car dimensions: 20 x 40; if player is less than 20 px to
        # the center of the car, then they collided
        if player.distance(c) < 20:
            # player.change_color_after_crash()
            scoreboard.game_over()
            game_is_on = False


    # after crossing the finish line
    if player.ycor() >= 285:
        player.return_to_start()
        scoreboard.level_up()
        car.increase_speed()


screen.exitonclick()
