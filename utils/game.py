from random import choice
from sys import exit
from typing import List
class Hangman:
    """This class is the settings for the Hangman game."""
    def __init__(self) -> None:
        self.possibles_words: List[str]=["becode","learning","mathematics","sessions","variable","function","algorithm","debugging","iteration","condition","operator","syntax","compiler","interpreter","recursion","object","class","method","inheritance","polymorphism","abstraction","encapsulation","database","version","git","javascript","python","java","csharp","html","css","php","sql","ruby","typescript","frontend","backend","server","framework","library","api","variable","boolean","integer","float","string","array","list","dictionary","tuple","module","package","import"]
        self.word_to_find: List[str] = list(random.choice(self.possibles_words))
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ["_" for e in self.word_to_find]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
    def play(self):
    """Play a single turn of the Hangman game.
    This method prompts the player to enter a letter and checks if it's in the word to find.
    If the guess is correct, it updates the game state, and if incorrect, it deducts a life.
    """
        print("the word to find has",len(self.word_to_find),"letters")
        guess: str = input("Enter a letter")
        while True:
            if len(guess) == 1 and guess.isalpha():
                if guess in self.word_to_find:
                    for index, letter in enumerate(self.word_to_find):
                        if letter == guess:
                            self.correctly_guessed_letters[index] = guess
                            self.turn_count += 1
                            print(guess," is in the word to find!") 
                    break #exit the loop if the guess is correct.         
 
                else:
                    print(guess,"is not in the word to find")
                    self.wrongly_guessed_letters.append(guess)
                    self.lives -= int(1)
                    self.error_count += int(1)
                    self.turn_count += int(1)
                    break #exit the loop if the guess is incorrect.
            else:
                print("Please enter only 1 letter, no digit or special character.")
                break #exit the loop if the input is incorrect. 
  
    
    def start_game(self):
        """Start the Hangman game"""
        while self.lives != 0 :
            self.play()
            if self.lives == 0:
                self.game_over()
            if ''.join(self.correctly_guessed_letters) == ''.join(self.word_to_find):
                self.well_played()
            else:
                print("Your guess:",''.join(self.correctly_guessed_letters), "the wrongly guessed letters are",self.wrongly_guessed_letters,",you have ", self.lives,"live(s) left",", you made ", self.error_count," error(s)",", the number of turn is:", self.turn_count)

    def game_over(self):
        """End the game and display a 'Game Over' message."""
        print("the word to find was",self.word_to_find, "\nGame over...")
        quit()


    def well_played(self):
        """End the game and display a 'Well Played' message."""
        print("You find the word", self.word_to_find, "in",self.turn_count,"turns, with",self.error_count,"error(s)")
        quit()
        






   