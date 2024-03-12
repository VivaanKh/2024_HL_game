def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks users response, question.
        # Repeats if users don't enter yes / no.
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no.")


def instruction():
    print('''
    
    **** Instructions ****

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

Good luck.

    ''')


# Main routine
print()
print(" ⬆⬆⬆ Welcome to the higher Lower game ⬇⬇⬇ ")
print()

# loop for testing purposes.

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")