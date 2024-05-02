import math
import random


# checks users enter yes (y) or no (n)
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
secret number will be between 1 and 10).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

Good luck.

    ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # Check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it.
            else:
                return response

        except ValueError:
            print(error)


# calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Game History / Statistics area.
# finds the lowest, highest and average score from a list
def get_stats(all_scores):
    # sort the lists.
    all_scores.sort()

    # find lowest, highest and average scores...
    worst_score = all_scores[0]
    best_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    return [worst_score, best_score, average_score]


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""
history_item = ""

game_history = []
all_scores = []

print(" ⬆⬆⬆ Welcome to the higher Lower game ⬇⬇⬇ ")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ",
                       low=1, exit_code="")

print("you chose: ", num_rounds)

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5
    print("Infinite Mode")
# ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? (0 - 10) ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose the high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num + 1)

# Calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
        num_rounds += 1
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)

    # Round starts here
    # set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)
    print("Spoiler Alert", secret)  # REMOVE THIS LINE AFTER TESTING.

    # increases number of rounds.
    rounds_played += 1

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number...
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want to quit
        if guess == "xxx":
            # set end_game to user so that outer loop can be broken
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        # if guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # add one to the number of guesses used
        guesses_used += 1

        # compare the user's guess with the secret number set up feedback statement

        # if we have guesses left...
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, please try a higher number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, please try a lower number."
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

        # when the secret number is guessed, we have three different feedback
        # option (lucky / 'phew' / well done)
        elif guess == secret:
            history_item = f"round: {rounds_played}: You got it in {guesses_used}"
            print(f"You got it in {guesses_used} guesses!")
            break

            # if there are no guesses left
        elif guesses_used == guesses_allowed:
            history_item = f"round: {rounds_played}: That was close, you got it in {guesses_used} guesses."
            break

        if guesses_used == 1:
            history_item = f"round: {rounds_played}: Lucky, you got it right on the first guess!"

        elif guesses_used == guesses_allowed:
            history_item = f"round: {rounds_played}: That was close, you got it in {guesses_used} guesses."

        else:
            history_item = f"round: {rounds_played}: Well done! you guessed the secret number" \
                           f" in {guesses_used} guesses."

        all_scores.append(guesses_used)
        # print feedback to user
        print(feedback)

        # additional feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1:
            print("\nCareful.. you have one guess left!\n")

    print()

    # Round ends here

    # if user has entered the exit code, end the game!
    if end_game == "yes":
        break

    game_history.append(history_item)

rounds_played += 1

# Game loop ends here

# calculate the lowest, highest and average
# scores and display them.
user_stats = get_stats(all_scores)

average_score = "{:.1f}".format(user_stats[2])

print("📊📊📊 Game Statistics 📊📊📊 ")
print(f"Best Score: {user_stats[0]}\t "
      f"Worst Score: {user_stats[1]}\t "
      f"Average Scores: {average_score}")



# Ask the user if they want to see their game history and if they do, print game history.
if rounds_played > 0:

    see_history = yes_no("\nDo you want to see your game history?\n")

    if see_history == "yes":
        print("\n⌛⌛⌛ Game History ⌛⌛⌛")

        for item in game_history:
            print(item)



