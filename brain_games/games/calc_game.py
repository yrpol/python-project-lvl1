import random
from py_expression_eval import Parser
parser = Parser()


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
