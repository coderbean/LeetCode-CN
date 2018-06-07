class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num = list()
        small_list = nums1
        large_list = nums2
        if len(nums1) > len(nums2):
            small_list = nums2
            large_list = nums1
        for i in range(len(small_list)):
            if small_list[i] in large_list:
                num.append(small_list[i])
                large_list.remove(small_list[i])

        return num


if __name__ == '__main__':
    solution = Solution()
    result = solution.intersect(nums1=[1, 2, 2, 1], nums2=[1])
    print(result)
