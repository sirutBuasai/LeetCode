class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                      
        d = {}
        idx = 0
        
        for n in nums:
          
          if n not in d.keys():
            d[n] = idx
            nums[idx] = n
            idx += 1
            
            
        return len(d.keys())
