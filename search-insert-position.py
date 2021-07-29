class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # 1 2 3 4 5 6 7 8 9 10
        # 0 1 2 3 4 5 6 7 8 9
        
        left = 0
        right = len(nums)
        
        while left < right:
          
          mid = left + ((right - left) // 2)
          
          if target > nums[mid]:
            left = mid + 1
            
          elif target < nums[mid]:
            right = mid
            
          else:
            return mid
          
        return left
      
