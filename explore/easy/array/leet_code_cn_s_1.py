class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 1
        while True:
            if index >= len(nums):
                break
            if nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index = index + 1

        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    result = solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(result)
