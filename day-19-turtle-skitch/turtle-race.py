import colorgram
import turtle
import random


def main():
    is_race_on = False
    screen = turtle.Screen()
    screen.title("Turtle Race!")
    screen.setup(width=600, height=600)
    user_bet = screen.textinput(title="Make a bet", prompt="Which Turtle will win the race? ")
    turtles_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    turtles = []
    
    for t_color in turtles_color:
        t = turtle.Turtle(shape="turtle")
        t.color(t_color)
        pos_y = -50 + (30 * turtles_color.index(t_color))
        t.penup()
        t.goto(x=-230, y=pos_y)
        turtles.append(t)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for t in turtles:
            if t.xcor() >= 280:                
                is_race_on = False
                winning_turtle = t.pencolor()
                if user_bet.lower() == winning_turtle:
                    print(f'You Won, the winning turtle: {winning_turtle}!')
                else:
                    print(f'You lose, the winning turtle: {winning_turtle}!')
            random_move = random.randint(0, 10)
            t.forward(random_move)


    screen.exitonclick()



if __name__ == "__main__":
    main()
