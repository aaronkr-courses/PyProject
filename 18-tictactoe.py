"""Tic-Tac-Toe, by Al Sweigart al@inventwithpython.com
The classic board game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, board game, game, two-player"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '  # 문자열 값에 대한 상수


def main():
    print('Welcome to Tic-Tac-Toe!')
    # 틱-택-토 보드 딕셔너리를 생성한다.
    # X가 먼저 나오고, 그 다음에 O가 나온다.

    


def getBlankBoard():
    """비어 있는 새로운 틱-택-토 보드를 생성한다."""
    # 빈칸에 대한 번호: 1|2|3
    #                -+-+-
    #                4|5|6
    #                -+-+-
    #                7|8|9
    # 키는 1부터 9이고, 값은 X, O, 또는 BLANK:
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # 모든 칸을 빈칸으로 시작한다.
    return board


def getBoardStr(board):
    """보드에 대한 텍스트를 반환한다."""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])

def isValidSpace(board, space):
    """보드의 공백이 유효한 공백 번호고 비어 있다면
    True를 반환한다."""
    


def isWinner(board, player):
    """플레이어가 TTT 보드의 승자라면 True를 반환한다."""
    # 가독성을 위해 여기에 사용된 짧은 변수 이름:
    b, p = board, player
    # 행 3개, 열 3개, 대각선 2개에 걸쳐 표시가 있는지 확인한다.
    return ((b['1'] == b['2'] == b['3'] == p) or  # 상단 행
            (b['4'] == b['5'] == b['6'] == p) or  # 중단 행
            (b['7'] == b['8'] == b['9'] == p) or  # 하단 행
            (b['1'] == b['4'] == b['7'] == p) or  # 왼쪽 열
            (b['2'] == b['5'] == b['8'] == p) or  # 중앙 열
            (b['3'] == b['6'] == b['9'] == p) or  # 오른쪽 열
            (b['3'] == b['5'] == b['7'] == p) or  # 대각선
            (b['1'] == b['5'] == b['9'] == p))    # 대각선

def isBoardFull(board):
    """보드의 모든 공간이 채워지면 True를 반환한다."""
    


def updateBoard(board, space, mark):
    """보드에 표시할 공간을 설정한다."""
    


if __name__ == '__main__':
    main()  # 이 모듈이 임포트되지 않고 실행된다면 main()이 호출된다.
