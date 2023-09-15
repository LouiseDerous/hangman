import random
import re
import sys
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
    #Methods

    # A play() method that asks the player to enter a letter. 
    # Be careful that the player shouldn't be allowed to type something else than a letter, and not more than a letter. 
    # If the player guessed a letter well, add it to the correctly_guessed_letters list. 
    # If not, add it to the wrongly_guessed_letters list and add 1 to error_count.
    def play(self):
        print("the word to find has",len(self.word_to_find),"letters")
        guess = input("Enter a letter")
        if len(guess) == 1 and guess.isalpha():
            if guess in self.word_to_find:
                for index, letter in enumerate(self.word_to_find):
                    if letter == guess:
                        self.correctly_guessed_letters[index] = guess
                        self.turn_count += 1
                        print(guess," is in the word to find!")           
 
            else:
                print(guess,"is not in the word to find")
                self.wrongly_guessed_letters.append(guess)
                self.lives -= int(1)
                self.error_count += int(1)
                self.turn_count += int(1)
        else:
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
            if ''.join(self.correctly_guessed_letters) == ''.join(self.word_to_find):
                self.well_played()
            else:
                print("Your guess:",''.join(self.correctly_guessed_letters), "the wrongly guessed letters are",self.wrongly_guessed_letters,",you have ", self.lives,"live(s) left",", you made ", self.error_count," error(s)",", the number of turn is:", self.turn_count)
            #else:
                #print(self.correctly_guessed_letters, self.wrongly_guessed_letters, self.lives, self.error_count, self.turn_count)
            

    #A game_over() method that will stop the game and print game over....
    def game_over(self):
        print("the word to find was",self.word_to_find, "\nGame over...")
        quit()

    #A well played() method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with 
    # {error_count_here} errors!.

    def well_played(self):
        print("You find the word", self.word_to_find, "in",self.turn_count,"turns, with",self.error_count,"error(s)")
        quit()
        






   