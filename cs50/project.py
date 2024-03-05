
import random
from pyfiglet import Figlet


def main():
    linux = ['kali', 'fedora', 'arch', 'ubuntu', 'mint', 'redhat', 'debian']
    textEditor = ['vim', 'emacs', 'vscode', 'vs', 'neovim', 'zed', 'notepad']
    cs50 = ['david', 'malan', 'karter', 'brain', 'rubberduck', 'cs50x', 'cs50p']

    while True:
        try:
            choose = int(input('-choose Words-\nLinux -> [1]\nText Editors -> [2]\nCS50 -> [3]\nQuit -> [0]\n[1/2/3] : '))

            if isValidChoice(choose):
                if choose == 0:
                    break
                elif choose == 1:
                    word = random.choice(linux)
                elif choose == 2:
                    word = random.choice(textEditor)
                else:
                    word = random.choice(cs50)

                attempts = 7
                guessedChars = []

                while attempts != 0:
                    current_game = displayWord(word, guessedChars)
                    print('Game: ', current_game)

                    get_char = input('char: ')

                    if get_char in guessedChars:
                        print('Already Guessed')
                        continue

                    guessedChars.append(get_char)

                    if get_char not in word:
                        attempts -= 1
                        print('Wrong')

                    if '_' not in displayWord(word, guessedChars):
                        print(printWinLoose('win'))
                        break

                if attempts == 0:
                    print(printWinLoose('lose'))
                    print('The word was, ', word)
            else:
                print('Invalid choice')
        except ValueError:
            pass


def isValidChoice(user):
    return user in [1, 2, 3, 0]


def printWinLoose(winLoose):
    figlet = Figlet()
    figlet.setFont(font='slant')
    stylized_text = figlet.renderText(winLoose)
    return stylized_text


def displayWord(word, guessed_char):
    display = ''

    for char in word:
        if char in guessed_char:
            display += char
        else:
            display += '_'
    return display


if __name__ == "__main__":
    main()
