class Player: # creates a player with name/unique symbol and sets win to False for loop control
    def __init__(self, name,symbol = "X"):
        self.name = name
        self.symbol = symbol
        self.win = False
    def __repr__(self):
        return "\n" + self.name + " = " + self.symbol + " win = " + str(self.win)

board = {
    "A": ["-","-","-"],
    "B": ["-","-","-"],
    "C": ["-","-","-"]
}
def menu():
    print("***************")
    print("*             *")
    print("* TIK TAC TOE *")
    print("*             *")
    print("***************")
    player1 = input("\nPlayer 1 what is your name:\n").title()
    symbol = input("\n" + player1 +" what symbol would you like?\nEnter X or O\n").upper()
    while symbol != 'X' and symbol != 'O':
      symbol = input('Invalid Entry\nPlease enter X or O\n').upper()
    player2 = input("\nPlayer 2 what is your name:\n").title()
    return player1, player2, symbol

def display_board():
    print("====================")
    print("       BOARD")
    for x in board:
        print(x, board[x])
    print("    0    1    2")
    print("====================")

def winner(p):
    p.win = True
    print("Congratulations " + p.name + " you have won!!!")
    display_board()

def check_tie(p):
    if '-' not in board['A'] and '-' not in board['B'] and '-' not in board['C']:
        display_board()
        print("There has been a Tie")
        p.win = True

def check_win(p):
    check_tie(p)
    if board["A"][0]==p.symbol and board["A"][1]== p.symbol and board["A"][2]==p.symbol:
        winner(p)
    elif board["B"][0]==p.symbol and board["B"][1]== p.symbol and board["B"][2]==p.symbol:
        winner(p)
    elif board["C"][0]==p.symbol and board["C"][1]== p.symbol and board["C"][2]==p.symbol:
        winner(p)
    elif board["A"][0]==p.symbol and board["B"][0]== p.symbol and board["C"][0]==p.symbol:
        winner(p)
    elif board["A"][1]==p.symbol and board["B"][1]== p.symbol and board["C"][1]==p.symbol:
        winner(p)
    elif board["A"][2]==p.symbol and board["B"][2]== p.symbol and board["C"][2]==p.symbol:
        winner(p)
    elif board["A"][0]==p.symbol and board["B"][1]== p.symbol and board["C"][2]==p.symbol:
        winner(p)
    elif board["A"][2]==p.symbol and board["B"][1]== p.symbol and board["C"][0]==p.symbol:
        winner(p)

def insert(coord, p):
    try:
      x, y = coord[0], int(coord[1])
      if p == p1:
        if board[x][y] == p2.symbol or board[x][y] == p.symbol:
            print("***That space is already occupied***")
            play(p)
        else:
            board[x][y] = p.symbol
            check_win(p)
      elif p == p2:
        if board[x][y] == p1.symbol or board[x][y] == p.symbol:
          print('***That space is already occupied***')
          play(p)
        else:
          board[x][y] = p.symbol
          check_win(p)
    except ValueError:#if input is a special character 
      print("***That was an invalid entry***")
      play(p)
    except:
      print("***That was an invalid entry***")
      play(p)


def play(p):
    coords = input(p.name + " which space would you like?\n").upper()
    while len(coords) > 3:
      print('***That was an invalid entry***')
      coords = input(p.name + ' which space would you like?\n').upper()
    insert(coords, p)


player1, player2, symbol = menu()
p1 = Player(player1, symbol)
if p1.symbol == "X":
    p2 = Player(player2, "O")
else:
    p2 = Player(player2)

while p1.win == False and p2.win == False:
    display_board()
    play(p1)
    if p1.win == True:
      break
    display_board()
    play(p2)

