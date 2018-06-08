class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            ans = haystack.index(needle)
        except ValueError:
            return -1
        return ans


if __name__ == '__main__':
    solution = Solution()
    result = solution.strStr(haystack="hello", needle="22")
    print(result)
