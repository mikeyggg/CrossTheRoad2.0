from turtle import Screen
from Player import Player
from cars import Car
from text import Text
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.tracer(0)
screen.colormode(255)


player = Player()

screen.onkey(player.go_up, "w")

screen.listen()
cars = []

max_cars = 15
current_cars = 0
car_counter = 0
level = 1

level_display = Text(level)

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)


    cars_to_remove = []
    car_counter += 1

    if len(cars) < max_cars and car_counter % 6 == 0:
        cars.append(Car(level))
        current_cars += 1


    for car in cars:
        car.advance()

        if car.xcor() < -260:
            car_counter -= 1
            current_cars -= 1
            car.hideturtle()
            cars_to_remove.append(car)

        if car.distance(player) < 30:
            game_over = True

    for car2 in cars_to_remove:
        cars.remove(car2)

    if player.ycor() > 380:
        level += 1
        player.hideturtle()
        player.goto(0,-380)
        player.showturtle()
        level_display.update_level()

        for car in cars:
            car.hideturtle()

        cars.clear()






screen.exitonclick()