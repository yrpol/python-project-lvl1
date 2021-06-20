import random


def gcd(a, b):
    numbers = (a, b)
    sorted_numbers = sorted(numbers)
    (b, a) = sorted_numbers

    if a % b == 0:
        return b
    return gcd(a % b, b)


def brain_gcd():
    condition = "Find the greatest common divisor of given numbers."

    def play_round():
        first_number = random.randint(1, 50)
        second_number = random.randint(1, 50)

        expression = "{} {}".format(first_number, second_number)
        correct_answer = str(gcd(first_number, second_number))
        return (expression, correct_answer)

    return condition, play_round
