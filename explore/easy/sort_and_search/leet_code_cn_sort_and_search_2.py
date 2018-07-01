# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
import sys

# 不知道为什么leetcode设置的默认递归层级很低，设置到100就可以AC了
sys.setrecursionlimit(100)  # 例如这里设置为十万


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif isBadVersion(1):
            return 1
        else:
            return self.binary_cut(0, n)

    def binary_cut(self, left, right):
        mid = (left + right) // 2
        if self.is_target(mid):
            return mid
        if self.is_target(mid + 1):
            return mid + 1
        elif isBadVersion(left) == isBadVersion(mid):
            return self.binary_cut(mid, right)
        else:
            return self.binary_cut(left, mid)

    def is_target(self, n):
        if isBadVersion(n) and not isBadVersion(n - 1):
            return True


def isBadVersion(version):
    if version == 1:
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.firstBadVersion(2)
    print(result)
