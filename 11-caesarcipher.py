"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

try:
    import pyperclip  # pyperclip은 텍스트를 클립보드로 복사한다.
except ImportError:
    pass  # 만약에 pyperclip이 설치되어 있지 않다면, 아무런 동작도 하지 않는다. 별일 아니다.

# 암호화/복호화할 수 있는 모든 기호:
# (!) 숫자와 문장 부호도 암호화할 수 있도록
# 여기에 추가해 보자.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# 암호화 또는 복호화할 문자를 사용자가 입력하게 하자:


# 사용할 키를 사용자가 입력하게 하자:


# 암호화/복호화하려는 메시지를 사용자가 입력하게 하자:


# 카이사르 암호는 대문자에서만 동작한다:


# 암호화/복호화된 형태의 메시지를 저장한다:


# 메시지의 각 기호를 암호화/복호화한다:


# 암호화/복호화된 문자열을 화면에 표시한다:

