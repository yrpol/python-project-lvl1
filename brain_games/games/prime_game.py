import random


def is_prime(num):
    if num == 1:
        return True

    def check(num, div):
        if num == div:
            return True
        elif num % div == 0:
            return False
        return check(num, div + 1)
    return check(num, 2)


def brain_prime():
    condition = "Answer 'yes' if given number is prime. Otherwise answer 'no'."

    def play_round():
        number = random.randint(1, 50)
        is_number_prime = is_prime(number)
        correct_answer = 'yes' if is_number_prime else 'no'
        return (number, correct_answer)

    return condition, play_round
