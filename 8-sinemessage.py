"""Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import math, shutil, sys, time

# 터미널 윈도우의 크기를 구한다:
WIDTH, HEIGHT = shutil.get_terminal_size()
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다:
WIDTH -= 1

print('Sine Message, by Al Sweigart al@inventwithpython.com')
print('(Press Ctrl-C to quit.)')
print()
print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')

