import random

class Hangman:

"""This class is the settings for the Hangman game."""
    #Attributes
    # contains a list of words. The list must also contain the following words :becode, learning, mathematics, sessions
    possibles_words = ["becode","learning","mathematics","sessions","variable","function","algorithm","debugging","iteration","condition","operator","syntax","compiler","interpreter","recursion","object","class","method","inheritance","polymorphism","abstraction","encapsulation","database","version","git","javascript","python","java","csharp","html","css","php","sql","ruby","typescript","frontend","backend","server","framework","library","api","variable","boolean","integer","float","string","array","list","dictionary","tuple","module","package","import"]
    # list of strings, each element will be a letter of the word
    word_to_find = random.choice(possibles_words.split())
    #attribute that contains the number of lives that the player still has left. It should start at 5.
    lives =
    # attribute that contains a list of strings where each element will be a letter guessed by the user. 
    correctly_guessed_letters =
    # A wrongly_guessed_letters attribute that contains a list of strings where each element will be a letter guessed by the user that is not in the word_to_find.
    wrongly_guessed_letters = 
    # A turn_count attribute that contain the number of turns played by the player. This will be represented as an int.
    turn_count = 
    # An error_count attribute that contains the number of errors made by the player.
    error_count = 
    #Methods

    # A play() method that asks the player to enter a letter. 
    # Be careful that the player shouldn't be allowed to type something else than a letter, and not more than a letter. 
    # If the player guessed a letter well, add it to the correctly_guessed_letters list. 
    # If not, add it to the wrongly_guessed_letters list and add 1 to error_count.
    def play ():

    #A start_game() method that:
        #will call play() until the game is over (because the use guessed the word or because of a game over).
        #will call game_over() if lives is equal to 0.
        #will call well_played() if all the letter are guessed.
        #will print correctly_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn
    
    def start_game(self):
        
    
    #A game_over() method that will stop the game and print game over....
    def game_over():
        if #condition:
            break
            print("Game over...")

    #A well played() method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with 
    # {error_count_here} errors!.

    def well_played():






   