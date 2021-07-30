class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest = float('inf')
        closest_val = 0
        
        for idx, val in enumerate(nums):
          
          if idx > 0 and val == nums[idx-1]:
            continue
          
          left = idx+1
          right = len(nums)-1
          
          while left < right:
            
            added = val +nums[left] + nums[right]
            
            if added > target:
              right -= 1
              temp = added - target
              
              if temp < closest:
                closest = temp
                closest_val = added
            
            else:
              left += 1
              temp = target - added
              
              if temp < closest:
                closest = temp
                closest_val = added
                
        return closest_val
      
