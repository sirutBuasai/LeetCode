class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        elif len(digits) == 1:
            return [1, 0]
        
        else:
            return self.plusOne(digits[0: len(digits)-1]) + [0]
          
