class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp = nums[0]
        ans = nums[0]
        
        for idx in range(1, len(nums)):
            
            temp = max(nums[idx], nums[idx] + temp)
            ans = max(ans, temp)
        
        return ans
      
