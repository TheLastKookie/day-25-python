import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=490)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

uncle_sam = turtle.Turtle()
uncle_sam.hideturtle()
uncle_sam.penup()

correct_guesses = []
all_states = states_data.state.to_list()

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="Give me a state's name if you dare.").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in correct_guesses:
        state_row = states_data[states_data.state == answer_state]
        uncle_sam.goto(int(state_row.x), int(state_row.y))
        uncle_sam.write(arg=answer_state, font=("Arial", 10, "normal"))
        correct_guesses.append(answer_state)
        screen.update()

states_to_learn_dict = {
    "state": [],
}

for state in all_states:
    if state not in correct_guesses:
        states_to_learn_dict["state"].append(state)

states_df = pandas.DataFrame(states_to_learn_dict)
states_df.to_csv("states_to_learn.csv")
