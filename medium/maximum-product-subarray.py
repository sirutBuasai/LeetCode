class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
          temp = curr_max

          curr_max = max(nums[i], curr_max*nums[i], curr_min*nums[i])
          curr_min = min(nums[i], temp*nums[i], curr_min*nums[i])

          max_product = max(curr_max, max_product)

        return max_product
