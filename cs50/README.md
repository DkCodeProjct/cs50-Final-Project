
# Word Guessng Game

#### Video Demo:  <https://youtu.be/Igw_Nq3OjeY>

#### Description:
In this Word Guessing Game, users can select a category from three options: 1. Linux Distros, 2. Text Editors, and 3. CS50. Upon choosing, a random word from the selected category is provided. Players have 7 attempts to guess the word, displayed as blank spaces ('_____') corresponding to the number of letters in the word. Correctly guessed letters are revealed in their respective positions. If the word isn't guessed within seven attempts, the game will be over.

## Project Files:
- `project.py`: The main Python script containing the game logic.
- `README.md`: Documentation for the project.
- `test_project.py`: test codes for 'isValidChoice' and 'displayWord' function

## Design Choices:
i use tree [] of words and random moduel to genarate a random word according to user choice, and another [] for tracking guessing char and user 2 functions to validate user inptu and, to show guessed word. also i use ptflight to print win and loose in ascci art.

## Installation:
To run the POS system, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/code50/148317495

TODO

choose Catogory:
-choose Words-
Linux -> [1]
Text Editors -> [2]
CS50 -> [3]
[1/2/3] :

after choose catogory, gussed letters:
Game:  ____
char:

if letter in words itll show the letter:
Game:  __K_

guessed letters  untill replace the '_' with letters, if all letters guessed correclty and no more '_', game over, if not you loose after 7 attempts

