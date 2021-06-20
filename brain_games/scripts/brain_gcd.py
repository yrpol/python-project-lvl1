#!/usr/bin/env python
from brain_games.games.gcd_game import brain_gcd
from brain_games.games.game_engine import welcome_user, start_game


def main():
    name = welcome_user()
    start_game(name, brain_gcd)


if __name__ == '__main__':
    main()
