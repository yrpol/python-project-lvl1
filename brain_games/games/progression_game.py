import random


def brain_progression():
    condition = "What number is missing in the progression?"

    def play_round():
        progression_length = 10
        step = random.randint(1, 7)
        first_number = random.randint(1, 15)
        hiden_number_index = random.randint(0, progression_length - 1)

        progression = ''
        correct_answer = ''
        current_number = str(first_number)
        index = 0

        while index < progression_length:
            if index == hiden_number_index:
                progression += '.. '
                correct_answer = current_number
            else:
                progression += '{} '.format(current_number)

            current_number = str(int(current_number) + step)
            index += 1

        return (progression, correct_answer)

    return condition, play_round
