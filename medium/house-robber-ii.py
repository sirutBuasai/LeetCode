class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_sublist(nums):
          if len(nums) <= 2:
            return max(nums)

          else:
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = nums[1]

          for i in range(2, len(dp)):
            dp[i] = max(dp[:i-1]) + nums[i]

          return max(dp[-1], dp[-2])

        if len(nums) <= 3:
          return max(nums)

        else:
          sub1 = rob_sublist(nums[:-1])
          sub2 = rob_sublist(nums[1:])

          return max(sub1, sub2)
