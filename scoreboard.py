from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1

    def show_level(self):
        self.clear()
        self.goto(-200, 270)
        self.write(f'Level: {self.level}', font={FONT})

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.penup()
        self.goto(-10, 0)
        self.color('red')
        self.write('Game Over', align='center', font={FONT})
