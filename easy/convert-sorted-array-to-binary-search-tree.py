class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
          return None

        lo = 0
        hi = len(nums)
        mid = (hi-lo) // 2
        root = TreeNode(val=nums[mid])

        root.left = self.sortedArrayToBST(nums[lo:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:hi])

        return root
