class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        s_list = list(s)
        d = dict()
        for i in range(len(s)):
            if s_list[i] in d.keys():
                d[s_list[i]] = d[s_list[i]] + 1
            else:
                d[s_list[i]] = 1

        for i in range(len(s)):
            if d[s_list[i]] == 1:
                return s_list.index(s_list[i])
        return -1


if __name__ == '__main__':
    solution = Solution()
    result = solution.firstUniqChar(s="leetcode")
    print(result)
