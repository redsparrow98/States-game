import turtle
import pandas

#####################  Screen  ###################
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
#we ad the shape of the images on the screen
screen.addshape(image)
#we change the shape of the turtle to the image
turtle.shape(image)

###################  Data frame  #################
data = pandas.read_csv("50_states.csv")

all_states = data["state"].to_list()

guessed_states = []

#####################  Game  ######################

while len(guessed_states) < 50:
    answer_state = screen.textinput \
        (title= f"{len(guessed_states)}/50 States Correct",\
            prompt="What's another State name").title()

    #if the answer is exit close the game and save the states not
    # guess in a list and convert it to a CSV file
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #check if the answer state is in the all states list and if it is write
    # the state name on the map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
