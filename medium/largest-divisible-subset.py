class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
      nums.sort()
      dp = [0 for _ in range(len(nums))]
      dp_i = [-1 for _ in range(len(nums))]
      best, best_i = -1, -1
      
      for i in range(len(nums)):
        for j in range(i):
          if nums[i] % nums[j] == 0 and dp[j] > dp[i]:
            dp[i] = dp[j]
            dp_i[i] = j
            
        dp[i] += 1
        if dp[i] > best:
          best, best_i = dp[i], i
          
      result = [nums[best_i]]
      while dp_i[best_i] > -1:
        best_i = dp_i[best_i]
        result.append(nums[best_i])
        
      return result
        
