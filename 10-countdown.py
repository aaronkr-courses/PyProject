"""Countdown, by Al Sweigart al@inventwithpython.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import sys, time
import sevseg  # 우리의 sevseg.py 프로그램을 임포트한다.

# (!) 초를 다른 숫자로 변경하자:
secondsLeft = 30

