import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def guess_number():
    answer = random.randint(1, 100)
    return answer


def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"you got it! the answer was {answer}")


def set_difficulty():
    level = input("choose a difficulty type 'easy' or 'hard'")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = guess_number()
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()