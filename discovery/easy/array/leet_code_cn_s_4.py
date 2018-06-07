class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.containsDuplicate(nums=[-1, -1, 3, 99])
    # result = solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    print(result)
