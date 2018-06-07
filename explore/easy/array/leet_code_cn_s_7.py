class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + temp
            temp = digits[i] // 10
            digits[i] = digits[i] % 10

        if temp > 0:
            digits.insert(0, temp)

        return digits


if __name__ == '__main__':
    solution = Solution()
    result = solution.plusOne(digits=[9, 9, 9, 9])
    print(result)
