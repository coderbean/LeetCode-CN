class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        x_set = set()
        y_set = set()
        for x in range(9):
            x_set.clear()
            y_set.clear()
            for y in range(9):
                if board[x][y] != '.':
                    if board[x][y] in x_set:
                        return False
                    else:
                        x_set.add(board[x][y])
                if board[y][x] != '.':
                    if board[y][x] in y_set:
                        return False
                    else:
                        y_set.add(board[y][x])

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if self.check_little_squre(board, [x, y]) is False:
                    return False

        return True

    def check_little_squre(self, board, cor):
        temp_set = set()
        for x in range(cor[0], cor[0] + 3):
            for y in range(cor[1], cor[1] + 3):
                if board[x][y] != '.':
                    if board[x][y] in temp_set:
                        return False
                    else:
                        temp_set.add(board[x][y])

        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.isValidSudoku(board=[
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ])
    print(result)
