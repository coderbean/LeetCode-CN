# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 108. Convert Sorted Array to Binary Search Tree 将有序数组转换为二叉搜索树
# 递归写代码，那叫一个爽
# 解题思路。每次在中间位置取出一个根节点，然后左右两边的数字重新组成数组，分别生成平衡二叉搜索树
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        mid_index = (len(nums) - 1) // 2
        root = TreeNode(nums[mid_index])
        root.left = self.sortedArrayToBST(nums[0:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index + 1:len(nums)])
        return root


if __name__ == '__main__':
    solution = Solution()
    result = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(result)
