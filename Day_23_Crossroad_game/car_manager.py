from turtle import Turtle, Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_SPEED = 5
MOVE_INCREMENT = 7


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.clear()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_SPEED
        self.live_turtle = True

    def create_car(self):
        if self.live_turtle:
            random_chance = random.randint(1, 6)
            if random_chance == 1:
                new_car = Turtle("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                random_y = random.randint(-250, 250)
                new_car.goto(320, random_y)
                self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        for car in self.all_cars:
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)

    def level_up(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed += MOVE_INCREMENT

    def collision(self):
        self.car_speed = 0
        self.live_turtle = False
