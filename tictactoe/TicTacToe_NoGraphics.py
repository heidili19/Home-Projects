import os

theBoard = {1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'}
winning_hands=[0b111000000,0b000111000,0b000000111,0b100100100,0b010010010,
               0b001001001,0b100010001,0b001010100]
def winner(board):
    #print(bin(board))
    for hand in winning_hands:
        if (hand & board) == hand:
            return True
    return False
'''    
def winning_dict()
    for board in range(0b1000000000)
        win_or_lose_dict = {}
        win_or_lose_dict[board] = whoWon(board)
'''    
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
printBoard(theBoard)

print(' ')

for i in range(10):
    theBoard[i] = ' ' 

print(' ')

x_board = 0
o_board = 0
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    while ((move == '' or theBoard[int(move)] is 'X') or
               (theBoard[int(move)] is 'O')):
        if move == '':
            print('Please input a numeric value, 1-9: ')
        else:
           print('That space is taken, please pick another space: ')
        move = input()            
    theBoard[int(move)] = turn
    if turn == 'X':
        x_board = x_board | (1<<(int(move)-1))
        if winner(x_board):
            printBoard(theBoard)
            print("X won!  Hooray X!!!")
            os._exit(0)
        turn = 'O'
    else:
        o_board = o_board | (1<<(int(move)-1))
        if winner(o_board):
            printBoard(theBoard)
            print("O won!  OH YEAH O!!!")
            os._exit(0)
        turn = 'X'
print("Booh, nobody won :-(.  A tie is like kissing your sister!")
