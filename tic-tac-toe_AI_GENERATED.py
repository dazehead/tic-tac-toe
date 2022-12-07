class Player:
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

class Game:
    def __init__(self):
        self.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player1 = Player("X")
        self.player2 = Player("O")

    def display_board(self):
        print("  1  2  3")
        print("1 " + self.game_board[0][0] + " | " + self.game_board[0][1] + " | " + self.game_board[0][2])
        print("  --------")
        print("2 " + self.game_board[1][0] + " | " + self.game_board[1][1] + " | " + self.game_board[1][2])
        print("  --------")
        print("3 " + self.game_board[2][0] + " | " + self.game_board[2][1] + " | " + self.game_board[2][2])

    def player_input(self, player):
        while True:
            row = int(input("Player " + player.marker + ", enter the row number (1-3): "))
            col = int(input("Player " + player.marker + ", enter the column number (1-3): "))
            if self.game_board[row-1][col-1] == " ":
                self.game_board[row-1][col-1] = player.marker
                break

    def check_win(self):
        # Check rows
        for row in self.game_board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != " ":
                return True

        # Check columns
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] and self.game_board[1][col] == self.game_board[2][col] and self.game_board[0][col] != " ":
                return True

        # Check diagonals
        if self.game_board[0][0] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][2] and self.game_board[0][0] != " ":
            return True
        if self.game_board[0][2] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][0] and self.game_board[0][2] != " ":
            return True

        # Check for tie
        for row in self.game_board:
            for col in row:
                if col == " ":
                    return False
        return "Tie"

def main():
    game = Game()
    while True:
        game.display_board()
        game.player_input(game.player1)
        if game.check_win():
            game.player1.score += 1
            print("Player " + game.player1.marker + " wins!")
            print("Player X: " + str(game.player1.score) + " | Player O: " + str(game.player2.score))
            game.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

            # Prompt the user to stop playing
            response = input("Do you want to keep playing? (y/n) ")
            if response.lower() == "n":
                break
            else:
                continue

        game.display_board()
        game.player_input(game.player2)
        if game.check_win():
            game.player2.score += 1
            print("Player " + game.player2.marker + " wins!")
            print("Player X: " + str(game.player1.score) + " | Player O: " + str(game.player2.score))
            game.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

            # Prompt the user to stop playing
            response = input("Do you want to keep playing? (y/n) ")
            if response.lower() == "n":
                break
            else:
                continue

        if game.check_win() == "Tie":
            print("It's a tie!")
            print("Player X: " + str(game.player1.score) + " | Player O: " + str(game.player2.score))
            game.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

            # Prompt the user to stop playing
            response = input("Do you want to keep playing? (y/n) ")
            if response.lower() == "n":
                break
            else:
                continue

main()
