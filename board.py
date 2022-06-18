import os
from tkinter import W

class Game:
    def __init__(self):
        self.board = [['.' for _ in range(20)] for _ in range(10)]
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
        self.update_player_pos(self.player_x, self.player_y - 1)

    def move_left(self):
        self.update_player_pos(self.player_x - 1, self.player_y)

    def move_down(self):
        self.update_player_pos(self.player_x, self.player_y + 1)

    def move_right(self):
        self.update_player_pos(self.player_x + 1, self.player_y)

def main():
    game = Game()
    game.update_board()

    while True:
        inp = input()

        if inp == 'w':
            game.move_up()
        elif inp == 'a':
            game.move_left()
        elif inp == 's':
            game.move_down()
        elif inp == 'd':
            game.move_right()

if __name__ == '__main__': main()
