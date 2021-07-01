import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
missed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Enter the state's name?").title()
    if answer_state == "Exit":
        for states in all_states:
            if states not in guessed_states:
                missed_states.append(states)
        new = pandas.DataFrame(missed_states)
        missed = new.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


#states_to_learn.csv






