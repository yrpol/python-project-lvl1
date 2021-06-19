#!/usr/bin/env python
from brain_games.games import welcome_user, start_game, brain_even


def main():
    name = welcome_user()
    start_game(name, brain_even)


if __name__ == '__main__':
    main()
