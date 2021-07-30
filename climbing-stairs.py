class Solution:
    def climbStairs(self, n: int) -> int:

        prev_fib = 1
        curr_fib = 1
        
        if n == 1:
          return curr_fib
        
        while n > 1:
          curr_fib += prev_fib
          prev_fib = curr_fib - prev_fib
          n -= 1
          
        return curr_fib
        
