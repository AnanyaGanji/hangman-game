Hangman Game 🕹️
This repository contains a simple Hangman Game implemented in Python. The player guesses letters to reveal a hidden word before running out of chances!

How to Play the Game 🎮

Objective:
-Guess the hidden word one letter at a time.
-You have a maximum of 6 wrong attempts to guess the word before you lose.

Gameplay:
-A random word is selected from a predefined list.
-Each letter guessed correctly will fill in the blanks for the word.
-Each incorrect guess brings you closer to losing the game by completing the hangman figure.

Winning and Losing:
-If you guess the word before the hangman figure is completed, you win! 🎉
-If the figure is fully drawn after 6 wrong guesses, you lose, and the word is revealed.

Requirements: 🛠️
To run the game, ensure you have:
Python 3.x installed on your system.

Features: ✨
-Randomly selects a word from a predefined list.
-Displays a graphical representation of the hangman figure as chances decrease.
-Allows the player to guess letters and provides feedback for each guess.
-Ends the game with a win or loss message based on the player's performance.

Rules of the Game: 📜
Correct Guess: Fills in the blanks with the guessed letter wherever it appears.
Incorrect Guess: Adds to the hangman figure and decreases remaining chances.
Win Condition: Guess all letters of the word before the hangman figure is complete.
Lose Condition: Fail to guess the word in 6 attempts.
