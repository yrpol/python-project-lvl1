#!/usr/bin/env python
from brain_games.games import welcome_user, brain_even


def main():
    name = welcome_user()
    brain_even(name)


if __name__ == '__main__':
    main()
