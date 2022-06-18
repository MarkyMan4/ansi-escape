import os
import sys
import termios
import tty

class Game:
    def __init__(self, board_rows, board_cols):
        self.board = [['.' for _ in range(board_rows)] for _ in range(board_cols)]
        self.player_y = int(len(self.board) / 2)
        self.player_x = int(len(self.board[0]) / 2)
        self.board[self.player_y][self.player_x] = '+'
        os.system('clear')

    def update_board(self):
        print('\033[1;1f', end='')
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')

            print()

    def update_player_pos(self, new_x, new_y):
        self.board[self.player_y][self.player_x] = '.'
        self.player_x = new_x
        self.player_y = new_y
        self.board[self.player_y][self.player_x] = '+'
        self.update_board()

    def move_up(self):
        if self.player_y > 0:
            self.update_player_pos(self.player_x, self.player_y - 1)

    def move_left(self):
        if self.player_x > 0:
            self.update_player_pos(self.player_x - 1, self.player_y)

    def move_down(self):
        if self.player_y < len(self.board) - 1:
            self.update_player_pos(self.player_x, self.player_y + 1)

    def move_right(self):
        if self.player_x < len(self.board[0]) - 1:
            self.update_player_pos(self.player_x + 1, self.player_y)

def get_char():
    """
    Get a single character from stdin without the user having to press enter
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def main():
    game = Game(20, 10)
    game.update_board()

    while True:
        inp = get_char()

        if inp == 'w':
            game.move_up()
        elif inp == 'a':
            game.move_left()
        elif inp == 's':
            game.move_down()
        elif inp == 'd':
            game.move_right()
        elif inp == 'q':
            sys.exit()

if __name__ == '__main__': main()
