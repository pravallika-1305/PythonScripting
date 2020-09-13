def setup():
    board = [[" " * 3 for i in range(3)]for j in range(3)]
    return board
def make_move(board,who,where):
    i,j = where
    #print(i,j)
    if board[i][j] == " ":
        board[i][j] = board[i][j].replace(board[i][j],who)
    return board
def get_transpose(board):
    transposed_board = [i for i in zip(*board)]
    return transposed_board
def iswin(board):
    symbol = [':']
    rows = [''.join(board[i]) for i in range(3)]
    cols = [''.join(x) for x in [_ for _ in zip(*rows)]]
    d1 = [''.join(board[i][i]) for i in range(3)]
    d2 = [''.join(board[i][2-i]) for i in range(3)]
    check = rows + symbol + cols + symbol + d1 + symbol + d2
    if "XXX" in check:
        return 'X'
    if "OOO" in check:
        return 'O'
    return ''


board = setup()
player1 = 'X'
player2 = 'O'
n = int(input("Enter the number of rows & columns:"))
position_list = [(i,j) for i in range(n) for j in range(n)]
final_dict = {x:position_list[x-1] for x in range(1,n**2 + 1)}

print("enter you choice from below:")
print(final_dict)
for moves in range(n ** 2):
    #if iswin(board) in 'XO':
        #print(iswin(board))
        #break
    choice = int(input())
    board =  make_move(board,'X',final_dict.get(choice))
    print(board)
    
    choice = int(input())
    board = make_move(board,'O',final_dict.get(choice))
    print(board)
    if iswin(board) in 'XO':
        print(iswin(board))
        break

   

