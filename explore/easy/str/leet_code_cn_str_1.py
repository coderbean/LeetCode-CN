class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        i = 0
        j = len(str_list) - 1
        while j > i:
            temp = str_list[i]
            str_list[i] = str_list[j]
            str_list[j] = temp
            i = i + 1
            j = j - 1

        return "".join(str_list)


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseString(s="hello")
    print(result)
