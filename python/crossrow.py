#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Board:
    def __init__(self):
        #self.board = [[1, 1, 0], [0, 0, 0], [0, 1, 0]]
        self.board = [[0, 0, 0, 1, 1, 0, 0, 1], 
                      [1, 0, 1, 1, 0, 0, 0, 1], 
                      [0, 1, 0, 1, 0, 0, 1, 1], 
                      [0, 0, 1, 0, 1, 1, 1, 0], 
                      [0, 1, 1, 0, 0, 0, 0, 1], 
                      [0, 1, 1, 0, 1, 0, 0, 1], 
                      [0, 1, 1, 0, 1, 0, 0, 1], 
                      [0, 0, 0, 0, 1, 1, 1, 0]]

    def check(self):
        #iterator = iter(iterator)
        #try:
        #    first = next(iterator)
        #except StopIteration:
        #    row_match = True
        #row_match = all(first == x for x in iterator)

        # Calculate row match
        for row in self.board:
            row_match = True
            first = row[0]
            for i in row:
                if i != first:
                    row_match = False
                    break
            if row_match:
                return True, first

        # Calculate Column match
        e = 0
        for element in self.board[0]:
            column_match = True
            first = self.board[0][e]
            for row in self.board:
                if row[e] != first:
                    column_match = False
                    break
            if column_match:
                return True, first
            e += 1

        # Calculate diagonal match
        x = 0
        first = self.board[x][x]
        diagonal_match = True
        for x in range(len(self.board) - 1):
            x += 1
            if self.board[x][x] != first:
                diagonal_match = False
                break
        if diagonal_match:
            return True, first

        x = len(self.board[0]) - 1
        y = len(self.board) - 1
        first = self.board[x][y]
        diagonal_match = True
        for x in range(len(self.board) - 1):
            x -= 1
            y -= 1
            if self.board[x][y] != first:
                diagonal_match = False
                break
        if diagonal_match:
            return True, first


        return False, None

    def check_wrapper(self):
        match, winner = self.check()
        if winner == 0:
            winner = 'O'
        else:
            winner = 'X'
        if match:
            print(f"{winner} WINS")
        else:
            print("Its a match")

    def display_board(self):
        for m in range(4 * len(self.board) + 1):
            print("-", end='')
        print()
        for row in self.board:
            for i in row:
                item = ""
                if i == 0:
                    item = 'O'
                else:
                    item = 'X'
                print(f"| {item} ", end='')
            print("|")
            for m in range(4 * len(self.board) + 1):
                print("-", end='')
            print()

if __name__ == "__main__":
    board = Board()
    board.display_board()
    board.check_wrapper()

