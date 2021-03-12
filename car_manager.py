from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # hide arrow in the middle of the screen
        self.hideturtle()

        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # in the main.py we set time.sleep(0.1), which makes our create_car() function run every 0.1 sec
        # this creates a lot of cars
        # so, create less:
        rand_num = random.randint(1, 6)
        if rand_num == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            # make turtle 20 x 40 in size
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            # our playing field is 600 x 600, which means: x-axis: -300 to 300, y-axis: -300 to 300
            # set y-coordinate as a random number
            new_car.goto(305, random.randint(-230, 250))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.back(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
