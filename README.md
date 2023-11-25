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
No additional installation is required except for Python. This game can be run in any standard Python environment.

## Usage
To play the game, run the script. The game will choose a random fruit from the list, and you will be prompted to guess the fruit one letter at a time. After each guess, the game will inform you if your guessed letter is in the word or not.

### Game Flow
1. A random fruit is chosen by the computer from a predefined list.
2. You are prompted to enter a single letter as your guess.
3. The game will respond whether your guessed letter is in the word.
4. Keep guessing letters until you can figure out the fruit or until you run out of guesses.

### Example
please enter a single letter as a guess: a
Good guess! a is in the word.

## File Structure
- `hangman.py`: The main Python script that contains the logic for the Hangman game.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).