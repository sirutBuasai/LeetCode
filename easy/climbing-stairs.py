class Solution:
    def climbStairs(self, n: int) -> int:

        prev_step = 1
        curr_step = 1

        if n == 1:
          return curr_step

        while n > 1:
          curr_step += prev_step
          prev_step = curr_step - prev_step
          n -= 1

        return curr_step
