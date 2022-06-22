class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxi = nums[0]

        for idx in range(1, len(nums)):
            curr = max(nums[idx], curr+nums[idx])
            maxi = max(maxi, curr)

        return maxi
