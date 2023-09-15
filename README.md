
# Hangman Game

This is a simple Hangman game implemented in Python. The game allows players to guess a randomly selected word within a limited number of attempts.

## Project Structure

The project is organized into two Python files:

1. `game.py`: Contains the `Hangman` class, which defines the game's logic and rules.

2. `main.py`: The main entry point of the program. It imports the `Hangman` class and initiates the game.

## Getting Started

To play the Hangman game, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/LouiseDerous/hangman
   ```

2. Navigate to the project directory:

   ```shell
   cd hangman-game
   ```

3. Run the game by executing `main.py`:

   ```shell
   python main.py
   ```

## How to Play

- The game will start with a randomly selected word, and you have a limited number of lives (default: 5).

- You need to guess one letter at a time by entering it when prompted.

- If your guess is correct, the letter will be revealed in the word, and you can continue guessing.

- If your guess is incorrect, the letter will be added to the list of wrongly guessed letters, and you'll lose a life.

- The game continues until you either:
  - Successfully guess the entire word.
  - Run out of lives.

## Game Over

- If you run out of lives, the game will display the correct word and end with a "Game Over" message.

- If you guess the entire word correctly, the game will display a "You found the word" message along with the statistics (turn count and error count) and then exit.

## Notes

- The list of possible words is predefined in the `Hangman` class, but you can modify it to include your own words. Currently, the list of possible words is about programming and computer science.  

- The game uses a simple text-based interface.

Enjoy playing Hangman!
```

