""" The random function being called """
import random

"""" The jumper class
The __init__ function gives the self.lives an equivalent of 4

The has_lives function has an if and else statements that 
return a true boolean if the __init__ function equivalent 
is greater than zero. If less than zero, the else statement 
returns false"""
class Jumper:

    def __init__(self):
        self.lives = 4

    def has_lives(self):
        if self.lives > 0:
            return True
        else: 
            return False
    
    def lose_a_life(self):
        self.lives -= 1

    
    

