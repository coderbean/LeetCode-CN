class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ans = list()
        index = 0
        while True:
            if index == len(strs[0]):
                return "".join(ans)
            temp = strs[0][index]
            for i in range(1, len(strs)):
                if index == len(strs[i]) or temp != strs[i][index]:
                    return "".join(ans)

            ans.append(strs[0][index])
            index = index + 1


if __name__ == '__main__':
    solution = Solution()
    result = solution.longestCommonPrefix(["dog", "doooo", "do"])
    print(result)
