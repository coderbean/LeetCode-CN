class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(i, length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(length):
            x = 0
            y = length - 1
            while x < y:
                temp = matrix[i][x]
                matrix[i][x] = matrix[i][y]
                matrix[i][y] = temp
                x = x + 1
                y = y - 1

        return matrix


if __name__ == '__main__':
    solution = Solution()
    result = solution.rotate([
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ])
    print(result)
