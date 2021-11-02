class Solution:
    def jump(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return 0
        
      max_jump = curr_jump = jump = 0
      for i in range(len(nums)-1):
        max_jump = max(max_jump, i + nums[i])
        if curr_jump == i:
          jump += 1                
          curr_jump = max_jump  
          
      return jump
          
