class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        old_nums = list(nums)
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    x = old_nums.index(nums[i])
                    y = old_nums.index(nums[j])
                    if x == y:
                        y = old_nums.index(nums[j], i + 1)
                    if x > y:
                        return [y, x]
                    else:
                        return [x, y]
                elif nums[i] + nums[j] > target:
                    break


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum(nums=[3, 3], target=6)
    print(result)
