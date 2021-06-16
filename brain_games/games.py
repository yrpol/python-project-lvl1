import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def brain_even(name):
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    round_count = 3
    while round_count > 0:
        current_number = random.randint(0, 20)
        is_number_even = current_number % 2 == 0
        correct_answer = 'yes' if is_number_even else 'no'

        print("Question: {}".format(current_number))
        answer = prompt.string("Your answer: ")

        round_result = correct_answer == answer

        if round_result:
            print("Correct!")
            round_count -= 1
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return False
    print("Congratulations, {}!".format(name))
