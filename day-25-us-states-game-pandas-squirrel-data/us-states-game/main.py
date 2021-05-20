import turtle
from numpy import tile
import pandas

image = "blank_states_img.gif"
states_df = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.setup(width=700, height=600)
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
state_writter = turtle.Turtle()
state_writter.hideturtle()
state_writter.penup()


def check_state(state):
    """check if state exists and returns its entry"""
    states = states_df["state"]
    return states_df[states == state]


user_guessed_states = []

while len(user_guessed_states) < 50:
    user_input = turtle.textinput(
        f"{len(user_guessed_states)}/50 States Correct",
        "what's another state name?"
    )    

    # Exit when cancled or type Exit
    # save missed states into a csv
    if not user_input or user_input.title() == "Exit":
        user_missed_states  = []
        states = states_df.state.to_list()

        for state in states:
            if state not in user_guessed_states:
                user_missed_states.append(state)

        pandas.DataFrame(user_missed_states).to_csv("states_to_learn.csv")
        break
    
    # check if the user input was correct and write that state on the map
    state_results = check_state(user_input.title())
    if not state_results.empty:
        x = int(state_results['x'])
        y = int(state_results['y'])
        state_name = state_results['state'].item()
        state_writter.goto(x, y)
        state_writter.write(state_name)
        user_guessed_states.append(state_name)
