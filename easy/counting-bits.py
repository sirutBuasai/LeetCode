class Solution:
    def countBits(self, n: int) -> List[int]:
      
        result = [0 for _ in range(n+1)]
        digit = 1
        count = 0
        for i in range(1,n+1):
          result[i] = result[count]+1
          count += 1
          
          if count == digit:
            digit *= 2
            count = 0
        
        return result
        
