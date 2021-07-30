class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      
        actual = 0
        expected = 0
        
        for x in nums:
          actual += x
      
        for y in range(len(nums)+1):
          expected += y
          
        return expected - actual
      
