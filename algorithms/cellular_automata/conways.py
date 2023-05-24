# simple terminal implementation of conways game of life

import os
import sys
import time
import random

class Game:
    def __init__(self, x, y, percentage_live, delay):
        self.x = x
        self.y = y
        self.board = []

        #self.initialize_top_row_board()
        self.initialize_random_board(percentage_live)

        self.time_delay = delay       # milliseconds
        self.empty_cell_char  = ' '
        self.filled_cell_char = '#'

        self.frame = ''

    def initialize_random_board(self, percentage_live):
        for i in range(self.y):
            current = []
            for j in range(self.x):
                r = random.randint(0, 100)
                if r <= percentage_live:
                    current.append(1)
                else:
                    current.append(0)
            self.board.append(current)

    def initialize_top_row_board(self):
        a = []
        for i in range(self.x):
            if i % 2 == 0:
                a.append(1)
            else:
                a.append(0)
        b = [0] * self.x
        for i in range(self.y - 12):
            self.board.append(b)

    def update_frame(self):
        text = '\n'
        for i in self.board:
            for j in i:
                if j == 1:
                    char = self.filled_cell_char
                else:
                    char = self.empty_cell_char
                text += f" {char}"
            text += '\n'
        self.frame = text

    def display(self):
        print(self.frame)

    def get_cell(self, x, y):
        if x >= 0 and x < len(self.board) and y >= 0 and y < len(self.board[0]):
            return self.board[x][y]
        return 0


    def next_cycle(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                try:
                    #count = self.board[row - 1][col - 1] + \
                    #        self.board[row - 1][col + 1] + \
                    #        self.board[row + 1][col - 1] + \
                    #        self.board[row + 1][col + 1] + \
                    #        self.board[row - 1][col]     + \
                    #        self.board[row + 1][col]     + \
                    #        self.board[row][col - 1]     + \
                    #        self.board[row][col + 1]

                    count = self.get_cell(row - 1, col - 1) + \
                            self.get_cell(row - 1, col + 1) + \
                            self.get_cell(row + 1, col - 1) + \
                            self.get_cell(row + 1, col + 1) + \
                            self.get_cell(row - 1, col    ) + \
                            self.get_cell(row + 1, col    ) + \
                            self.get_cell(row,     col - 1) + \
                            self.get_cell(row,     col + 1)

                    old = self.get_cell(row, col)

                except IndexError:
                    pass

                if old == 0:
                    if count == 3:
                        self.board[row][col] = 1
                else:
                    if count < 2 or count > 3:
                        self.board[row][col] = 0

    def run(self):
        while True:
            os.system("clear")
            #print("\x1B[2J")
            self.display()
            self.next_cycle()
            self.update_frame()
            time.sleep(self.time_delay / 1000)

# main

if __name__ == "__main__":

    if len(sys.argv) < 5:
        print("usage: conways.py <x> <y> <%liveinitial> <delay>")
        exit(0)

    game = Game(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    game.run()

