from project import displayWord, isValidChoice, printWinLoose
from unittest.mock import patch
import pytest
from project import Figlet, printWinLoose


def test_displayWord_1():

    word = "hello"
    guessed_char = ['h', 'e', 'l']

    result = displayWord(word, guessed_char)

    assert result == "hell_", "Test failed!"
    print("Test passed!")


def test_isValidChoice_2():
    assert isValidChoice(1) == True
    assert isValidChoice(2) == True
    assert isValidChoice(3) == True
    assert isValidChoice(0) == True
    assert isValidChoice(4) == False
    assert isValidChoice(-1) == False
    assert isValidChoice('invalid') == False


def test_printWinLoose_3():

    input_text = "Test"

    class MockFiglet:
        def setFont(self, font):
            pass

        def renderText(self, text):
            return f"<stylized version of '{text}'>"

    with patch("project.Figlet", MockFiglet):

        output = printWinLoose(input_text)

        assert f"<stylized version of '{input_text}'>" in output, f"Stylized output not found in {output}"
