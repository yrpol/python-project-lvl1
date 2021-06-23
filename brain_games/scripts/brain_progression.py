#!/usr/bin/env python3
from brain_games.games.progression_game import brain_progression
from brain_games.games.game_engine import welcome_user, start_game


def main():
    name = welcome_user()
    start_game(name, brain_progression)


if __name__ == '__main__':
    main()
