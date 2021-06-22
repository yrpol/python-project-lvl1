import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def start_game(name, game):
    (condition, play_round) = game()
    print(condition)

    round_count = 3
    while round_count > 0:
        (expression, correct_answer) = play_round()

        question = "Question: {}".format(expression)
        print(question)
        player_answer = prompt.string("Your answer: ")

        if player_answer == correct_answer:
            print("Correct!")
            round_count -= 1
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(player_answer,
                                                    correct_answer))
            print("Let's try again, {}!".format(name))
            return False
    print("Congratulations, {}!".format(name))
