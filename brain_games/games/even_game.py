import random


def brain_even():
    condition = "Answer 'yes' if the number is even, otherwise answer 'no'."

    def play_round():
        expression = random.randint(0, 20)
        is_number_even = expression % 2 == 0
        correct_answer = 'yes' if is_number_even else 'no'
        return (expression, correct_answer)

    return condition, play_round
