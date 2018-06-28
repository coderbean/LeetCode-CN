class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        x = m - 1
        y = n - 1
        index = m + n - 1
        while y > -1:
            # 还是一些边界条件的判断
            if x == -1 or nums1[x] < nums2[y]:
                nums1[index] = nums2[y]
                nums2[y] = 0
                y = y - 1
            else:
                nums1[index] = nums1[x]
                nums1[x] = 0
                x = x - 1

            index = index - 1


if __name__ == '__main__':
    solution = Solution()
    num1 = [2, 0]
    num2 = [1]
    result = solution.merge(num1, 1, num2, 1)
    print(num1)
