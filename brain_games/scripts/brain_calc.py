#!/usr/bin/env python
from brain_games.games import welcome_user, start_game, brain_calc


def main():
    name = welcome_user()
    start_game(name, brain_calc)

if __name__ == '__main__':
    main()
