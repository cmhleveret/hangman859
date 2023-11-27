# Hangman Python Game

## Table Of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [License](#license)

## Introduction
This Hangman game is a Python implementation where the computer randomly selects a fruit from a predefined list, and the user tries to guess it one letter at a time. It's a simple and interactive way to play the classic word-guessing game.

## Installation
No additional installation is required except for Python. This game can be run in any standard Python environment with the following command:
```python3 milestone_5.py```

## Usage
To play the game, run the script. The game will choose a random fruit from the list, and you will be prompted to guess the fruit one letter at a time. After each guess, the game will inform you if your guessed letter is in the word or not.

### Game Flow
1. A random fruit is chosen by the computer from a predefined list.
1. You are prompted to enter a single letter as your guess.
1. The game will respond whether your guessed letter is in the word.
1. Incorrect guesses reduce the number of lives.
1. Keep guessing letters until you figure out the fruit or run out of lives.

### Example
please enter a single letter as a guess: a
Good guess! a is in the word.

## File Structure
- `milestone_5.py`: The main Python script that contains the logic for the Hangman game.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).