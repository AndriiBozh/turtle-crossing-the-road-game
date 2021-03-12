from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def return_to_start(self):
        self.goto(STARTING_POSITION)

    # def change_color_after_crash(self):
    #     self.pencolor('red')
