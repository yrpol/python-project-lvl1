import prompt
import random
from py_expression_eval import Parser
parser = Parser()


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
    
        question = "Quesion: {}".format(expression)
        print(question)
        player_answer = prompt.string("Your answer: ")

        if  player_answer == correct_answer:
            print("Correct!")
            round_count -= 1
        else: 
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(player_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return False
    print("Congratulations, {}!".format(name))


def brain_even():
    condition = "Answer 'yes' if the number is even, otherwise answer 'no'."
    
    def play_round():
        expression = random.randint(0, 20)
        is_number_even = expression % 2 == 0
        correct_answer = 'yes' if is_number_even else 'no'
        return (expression, correct_answer)
    
    return condition, play_round


def brain_calc():
    condition = "What is the result of the expression?"
    def play_round():
        operators = ['*', '+', '-']
        first_number = random.randint(0, 10)
        second_number = random.randint(0, 10)
        current_operator = operators[random.randint(0, 2)]

        expression = "{} {} {}".format(first_number, current_operator, second_number)
        correct_answer = str(parser.parse(expression).evaluate({}))
        
        return (expression, correct_answer)
        
    return condition, play_round
