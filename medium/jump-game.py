class Solution:
    def canJump(self, nums: List[int]) -> bool:
      jump = nums[0]
      if jump == 0:
        return len(nums) == 1
      
      for i in range(1, len(nums)-1):
        jump = max(jump-1, nums[i])
        if jump == 0:
          return False
      return True
          
