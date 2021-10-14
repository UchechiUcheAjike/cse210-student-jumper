class Console:
    def read(self, prompt):
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            float: The user's input as a float.
        """
        return float(input(prompt))

    def write(self, text):
        print(text)

    def print_jumper(self, lives):
        if lives >= 4:
            print("  ___")
        if lives >= 3:
            print(" /___\")
        if lives >= 2:
            print(" \   /")
        if lives >= 1:
            print("  \ /")
            print("   0")
        if lives == 0:
            print("   x")
        print("  /|\")
        print("  / \")
        print()
        print("^^^^^^^")

    def display_guess(self, word):
        len(word)





        
            
    
