# implementation of 3 in a row

import os
import sys

class Game:
    def __init__(self, n):

        self.display_grid_numbers = True

        self.empty_char = '*'
        self.x_char     = 'X'
        self.o_char     = 'O'

        # 0 - empty
        # 1 - X
        # 2 - O

        self.board = []

        print(n)

        for i in range(n):
            current = []
            for j in range(n):
                current.append(0)
            self.board.append(current)

        '''
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        self.board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        '''

    def update(self, x, y, player):
        n = len(self.board) - 1
        if x > n or y > n:
            return 1
        if self.board[y][x] != 0:
            return 1
        self.board[y][x] = player
        return 0

    def get_status(self):

        # horizontal match

        for row in self.board:
            match = True
            first = row[0]
            for element in row:
                if element != first:
                    match = False
            if match:
                if first != 0:
                    return first

        # vertical match

        for i in range(len(self.board) - 1):
            match = True
            first = self.board[0][i]
            for row in self.board:
                if row[i] != first:
                    match = False
            if match:
                if first != 0:
                    return first

        # diagonal match

        match = True
        first = self.board[0][0]
        for i in range(len(self.board)):
            if self.board[i][i] != first:
                match = False
        if match:
            if first != 0:
                return first

        match = True
        first = self.board[0][len(self.board) - 1]
        for y in range(len(self.board)):
            x = len(self.board) - y - 1
            if self.board[y][x] != first:
                match = False
        if match:
            if first != 0:
                return first
        return 0

    def represent_element(self, element):
        if element == 0:
            return self.empty_char
        elif element == 1:
            return self.x_char
        elif element == 2:
            return self.o_char
        else:
            return "invalid"

    def display(self):

        os.system("clear")

        if self.display_grid_numbers:
            print("    ", end='')
            for i in range(len(self.board)):
                print(f" {i + 1} ", end='')
            print("\n    ", end='')
            for i in range(len(self.board)):
                print("---", end='')
            print()

        counter = 1
        for row in self.board:

            if self.display_grid_numbers:

                space = ''
                for i in range(len(str(len(self.board))) - len(str(counter))):
                    space += ' '

                print(f" {counter} {space}|", end='')
                counter += 1
            for element in row:
                x = self.represent_element(element)
                print(f" {x} ", end='')
            print()
        print()

    def user_interface(self):
        turn = 1
        while True:
            self.display()
            while True:
                try:
                    move = input(f" {self.represent_element(turn)} > ")
                    split = move.split(' ')
                    err = self.update(int(split[0]) - 1, int(split[1]) - 1, turn)
                    if err != 0:
                        print("invalid input")
                        continue
                except ValueError:
                    print("invalid input")
                    continue
                break
            status = self.get_status()
            if status != 0:
                self.display()
                print(f" ===========\n | {self.represent_element(status)} wins! |\n ===========")
                break
            if turn == 1:
                turn = 2
            else:
                turn = 1

if __name__ == "__main__":
   
    n = 3

    try:
        n = int(sys.argv[1])
    except:
        pass

    game = Game(n)
    game.user_interface()

