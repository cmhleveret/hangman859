import random

list_of_fruits = ['apple', 'pear', 'banana', 'orange', 'pineapple']
num_lives = 5

class Hangman():
    def __init__(self,list_of_fruits, num_lives):
        self.word_list = list_of_fruits
        self.num_lives = num_lives
        self.word = random.choice(list_of_fruits)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        self.word_guessed = ['_' for char in self.word]
        self.input_string = ''

    def check_guess(self, input_string):
        input_string = input_string.lower()
        print(f"input {input_string}")
        if input_string in self.word:
            print(f"Good guess! {input_string} is in the word.")
            self.list_of_guesses.append(input_string)
            for index, character in enumerate(self.word):
                if input_string == self.word[index]:
                    self.word_guessed[index] = character
                    print(self.word_guessed)
            return
        else:
            print(f"Sorry, {input_string} is not in the word. Try again.")
            self.list_of_guesses.append(input_string)
            self.num_lives = self.num_lives - 1
            print(f"You have {self.num_lives} lives left.")
            return

    def ask_for_input(self):
        is_valid_input = False
        while(not is_valid_input):
            self.input_string = input('please enter a single letter as a guess')
            if len(self.input_string) != 1:
                print("Invalid letter. Please, enter a single character.")
            elif not self.input_string.isalpha():
                print("Invalid letter. Please, enter a alphabetical character.")
            elif self.input_string in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                print(f"Success input string {self.input_string}")
                is_valid_input = True 
        return self.check_guess(self.input_string)

def play_game(list_of_fruits, num_lives):
    hangman_game = Hangman(list_of_fruits, num_lives)
    playing = True
    while playing:
        if hangman_game.num_lives < 1:
            playing = False
            print ('You lost!')
        elif (not '_' in hangman_game.word_guessed) & hangman_game.num_lives > 0:
            playing = False
            print ('Congratulations. You won the game!')
        else:
            hangman_game.ask_for_input()
    return 

play_game(list_of_fruits, num_lives)
