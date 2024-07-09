"""Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, card game"""

import random, sys

# 상수 설정:
HEARTS   = chr(9829) # 문자 9829는 '♥'.
DIAMONDS = chr(9830) # 문자 9830은 '♦'.
SPADES   = chr(9824) # 문자 9824는 '♠'.
CLUBS    = chr(9827) # 문자 9827은 '♣'.
# (chr 코드에 대한 목록은 https://inventwithpython.com/charactermap을 참조하자)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.''')

    money = 5000
    # 메인 게임 루프
        


# def getBet(maxBet):
"""플레이어에게 이번 판에 얼마를 걸지 묻는다."""
    


# def getDeck():
"""52개의 모든 카드에 대한 (rank, suit) 튜플 리스트를 반환한다."""
    


# def displayHands(playerHand, dealerHand, showDealerHand):
"""플레이어와 딜러의 카드를 보여준다.
    만약에 showDealerHand가 False이면, 딜러의 첫 번째 카드를 가린다."""
    


# def getHandValue(cards):
"""카드의 값을 반환한다. 얼굴이 있는 카드들은 모두 10이며,
    에이스는 11 또는 1이다(이 함수는 최적의 에이스 값을 선택한다)."""
    


# def displayCards(cards):
"""카드 리스트에 있는 모든 카드를 표시한다."""
    


# def getMove(playerHand, money):
"""플레이어 차례에서 플레이어 선택을 묻는다.
    히트인 'H', 스탠드인 'S', 더블 다운인 'D'를 반환한다."""
    
    

# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
