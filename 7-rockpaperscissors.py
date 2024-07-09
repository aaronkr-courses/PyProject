"""Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
The classic hand game of luck.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, game"""

import random, time, sys

print('''Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# 이들 변수는 승리, 패배, 무승부의 횟수를 추적한다.
wins = 0
losses = 0
ties = 0

# 메인 게임 루프
