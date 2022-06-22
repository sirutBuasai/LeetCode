class Solution:
    def reverse(self, x: int) -> int:
      def math_reverse(num):
        mult = 10**(len(str(num))-1)
        res = 0
        while num > 0:
          digit = num % 10
          res += (digit*mult)
          num //= 10
          mult //= 10

        return res

      if x < 10 and x > -10:
        return x

      ans = math_reverse(abs(x))
      if x < 0:
        if (ans*-1) < (-2**31):
          return 0
        else:
          return ans*-1

      if ans > ((2**31)-1):
        return 0
      else:
        return ans
