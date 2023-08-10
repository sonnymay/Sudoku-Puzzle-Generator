import random

class SudokuGenerator:

    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def print_board(self):
        for row in self.board:
            print(row)

    def is_valid_move(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + startRow][j + startCol] == num:
                    return False

        return True

    def solve_board(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            self.board[row][col] = num
                            if self.solve_board():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def generate_puzzle(self, num_holes=40):
        for _ in range(num_holes):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.board[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.board[row][col] = 0
        return self.board


if __name__ == '__main__':
    generator = SudokuGenerator()
    generator.solve_board()
    generator.print_board()  # Print the full Sudoku board
    print("---------------------")
    generator.generate_puzzle()
    generator.print_board()  # Print the Sudoku puzzle
