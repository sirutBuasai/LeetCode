class Solution:
    def fib(self, n: int) -> int:

        prev_fib = 0
        curr_fib = 1

        if n == 0:
          return prev_fib
        elif n == 0:
          return curr_fib

        while n > 1:
          curr_fib += prev_fib
          prev_fib = curr_fib - prev_fib
          n -= 1

        return curr_fib
