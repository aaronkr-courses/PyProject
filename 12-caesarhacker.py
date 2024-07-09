"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# 해킹할 메시지를 사용자가 입력하게 하자:


# 암호화/복호화할 수 있는 가능한 모든 기호:
# (이것은 메시지를 암호화할 때 사용했던 SYMBOLS와 일치해야 한다.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

