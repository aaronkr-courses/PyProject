"""Hangman, by Al Sweigart al@inventwithpython.com
Guess the letters to a secret word before the hangman is drawn.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, word, puzzle"""

# 이 게임은 "Invent Your Own Computer Games with Python" 책에도 나와 있다.
# https://nostarch.com/inventwithpython

import random, sys

# 상수 설정하기:
# (!) HANGMAN_PICS의 문자열을 추가하거나 변경하여
# 교수대를 기요틴으로 바꿔 보자.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# (!) 새로운 문자열을 가진 CATEGORY와 WORDS로 교체해 보자.
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


# def main():
#     print('Hangman, by Al Sweigart al@inventwithpython.com')

   


# def drawHangman(missedLetters, correctLetters, secretWord):
"""비밀 단어에 대해 맞힌 글자와 틀린 글자와 함께
    교수형 집행인의 현재 상태를 그린다."""
    


# def getPlayerGuess(alreadyGuessed):
"""플레이어가 입력한 문자를 반환한다. 
    이 함수는 플레이어가 이전에 추측하지 않은 문자를 입력했는지 확인한다."""
    


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:

