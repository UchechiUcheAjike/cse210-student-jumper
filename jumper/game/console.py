class Console:

    def get_guess(self, prompt):
        return input(prompt)    # may need to be char(input(prompt))

    def display_jumper(self, lives):
        if lives >= 4:
            print("  ___")
        if lives >= 3:
            print(" /___\\")
        if lives >= 2:
            print(" \   /")
        if lives >= 1:
            print("  \ /")
            print("   0")
        if lives == 0:
            print("   x")
        print("  /|\\")
        print("  / \\")
        print()
        print("^^^^^^^")

    def display_word(self, word, guessed_characters):

        display_word = ""
        for i in range(len(word)):
            if guessed_characters[i]:
                display_word += word[i]
            else:
                display_word += "_"
            display_word += " "
        print(display_word)
    
    def display_game_over(self, game_over_state):
        if game_over_state == 1:
            print("The Jumper has died! You lose!")
        
        if game_over_state == 2:
            print("You guessed the word! You win!")





        
            
    
