from game.console import Console
from game.guesser import Guesser
from game.jumper import Jumper

import random

class Director:
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.puzzle_list = ["apple", "banana", "orange", "grape", "lemon"]
        self.console = Console()
        self.guesser = Guesser()
        self.game_over = 0 # 0: still playing.    1: loss   2: win
        self.jumper = Jumper()
        self.chosen_word = ""
        self.guessed_characters = []
        self.current_letter = ""

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.chosen_word = self.choose_word()
        self.do_outputs()

        while not self.game_over:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.current_letter = self.console.get_guess("Guess a letter: ")

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        if self.current_letter in self.chosen_word:
            for i in range(len(self.chosen_word)):
                if self.current_letter == self.chosen_word[i]:
                    self.guessed_characters[i] = True
        else:
            self.jumper.lose_a_life()
        
        if self.jumper.lives <= 0:
            self.game_over = 1  # 1: loss

        if self.check_for_win():
            self.game_over = 2  # 2: win

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        self.console.display_word(self.chosen_word, self.guessed_characters)
        self.console.display_jumper(self.jumper.lives)
        if self.game_over:
            self.console.display_game_over(self.game_over)

    def choose_word(self):
        word = self.puzzle_list[random.randint(0, len(self.puzzle_list))]   #choose a random word
        for i in range(len(word)):  
            self.guessed_characters.append(False)           # populate list of guessed characters 
        return word
    
    def check_for_win(self):
        for i in range(len(self.guessed_characters)):
            if self.guessed_characters[i] == False:
                return False
            
        return True