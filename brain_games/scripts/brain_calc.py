#!/usr/bin/env python
from brain_games.games.calc_game import brain_calc
from brain_games.games.game_engine import welcome_user, start_game


def main():
    name = welcome_user()
    start_game(name, brain_calc)


if __name__ == '__main__':
    main()
