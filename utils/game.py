import random
import re

class Hangman:
    """This class is the settings for the Hangman game."""
    def __init__(self) -> None:
        self.possibles_words = ["becode","learning","mathematics","sessions","variable","function","algorithm","debugging","iteration","condition","operator","syntax","compiler","interpreter","recursion","object","class","method","inheritance","polymorphism","abstraction","encapsulation","database","version","git","javascript","python","java","csharp","html","css","php","sql","ruby","typescript","frontend","backend","server","framework","library","api","variable","boolean","integer","float","string","array","list","dictionary","tuple","module","package","import"]
        self.word_to_find = list(random.choice(self.possibles_words))
        self.lives = 5
        self.correctly_guessed_letters = ["_" for e in self.word_to_find]
        self.wrongly_guessed_letters = []
        self.turn_count = int(0)
        self.error_count = int()
        #modification test



    
    #Methods

    # A play() method that asks the player to enter a letter. 
    # Be careful that the player shouldn't be allowed to type something else than a letter, and not more than a letter. 
    # If the player guessed a letter well, add it to the correctly_guessed_letters list. 
    # If not, add it to the wrongly_guessed_letters list and add 1 to error_count.
    def play(self):
        guess = input("Enter a letter")
        if guess == len(1) and guess.isalpha():
            if guess in self.word_to_find:
                for guess, index in enumerate (self.word_to_find):
                    self.correctly_guessed_letters[index] = guess
            else:
                self.wrongly_guessed_letters.append(guess)
                self.lives -= 1
                self.error_count += int(1)
        else:
            guess = input("Enter a letter")
        self.turn_count += int(1)
        

           
        

    #A start_game() method that:
        #will call play() until the game is over (because the use guessed the word or because of a game over).
        #will call game_over() if lives is equal to 0.
        #will call well_played() if all the letter are guessed.
        #will print correctly_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn
    
    def start_game(self):
        while self.lives != 0 :
            self.play()
            if self.lives == 0:
                self.game_over()
            if re.match(self.correctly_guessed_letters,self.word_to_find):
                self.well_played()
            else:
                print(self.correctly_guessed_letters, self.wrongly_guessed_letters, self.lives, self.error_count, self.turn_count)
            

    #A game_over() method that will stop the game and print game over....
    def game_over(self):
        print("Game over...")
        quit

    #A well played() method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with 
    # {error_count_here} errors!.

    def well_played(self):
        print("You find the word", self.word_to_find, "in",self.turn_count, "with",self.error_count,"error")
        






   