from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.update_scoreboard()
        self.hideturtle()
        self.goto(x=0, y=270)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def track_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


