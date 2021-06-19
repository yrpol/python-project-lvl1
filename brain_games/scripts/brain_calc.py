#!/usr/bin/env python
from brain_games.games import welcome_user, brain_calc


def main():
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main__':
    main()
