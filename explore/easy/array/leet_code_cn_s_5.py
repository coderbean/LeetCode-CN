class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                nums_set.remove(nums[i])
            else:
                nums_set.add(nums[i])

        return nums_set.pop()


if __name__ == '__main__':
    solution = Solution()
    result = solution.singleNumber(nums=[4, 1, 2, 1, 2])
    # result = solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    print(result)
