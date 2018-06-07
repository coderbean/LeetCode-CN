# 思路：首先找到最左的0，然后记录下索引，将不为0的移到该位置同时将原来的位置设置为0，保持index只想最左的0
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)):
            if nums[i] == 0 and index < 0:
                index = i
            elif nums[i] != 0 and index >= 0:
                nums[index] = nums[i]
                nums[i] = 0
                while True:
                    index = index + 1
                    if nums[index] == 0:
                        break


if __name__ == '__main__':
    solution = Solution()
    result = solution.moveZeroes(nums=[0, 1, 0, 3, 12])
    print(result)
