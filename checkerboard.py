#This Ain't Your Grandpa's Checkerboard: Kattis

def rowsToColumns(board):
    size = len(board)
    builder = ''
    result = []
    for i in range(size):
        for j in range(size):
            builder += board[j][i]
        result.append(builder)
        builder = ''
        
    return result

def hasBalancedElements(entry):
    W, B = 0, 0
    for letter in entry:
        if letter == 'W':
            W+=1
        else:
            B+=1
    return B==W

def passesBalancedElements(board):
    for entry in board:
        if not hasBalancedElements(entry):
            return False
    return True

def passesRowConsecutive(board):
    for i in board:
        if 'WWW' in i or 'BBB' in i:
            return False
    return True

def passesColumnConsecutive(board):
    board = rowsToColumns(board)
    return passesRowConsecutive(board)


def main():
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    if passesRowConsecutive(board) and passesColumnConsecutive(board):
        if passesBalancedElements(board) and passesBalancedElements(rowsToColumns(board)):
            print(1)
        else:
            print(0)
    else:
        print(0)

main()
