class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, len(nums) - k, len(nums))
        self.reverse(nums, 0, len(nums) - k)
        self.reverse(nums, 0, len(nums))
        return nums

    def reverse(self, nums, l, r):
        i = l
        j = r - 1
        while j > i:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i = i + 1
            j = j - 1


if __name__ == '__main__':
    solution = Solution()
    result = solution.rotate(nums=[-1, -100, 3, 99], k=2)
    # result = solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    print(result)
