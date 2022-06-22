class Solution:
    def multiply(self, num1: str, num2: str) -> str:
      def convert_int(string):
        i = len(string)-1
        digit = 1
        n = 0
        while i >= 0:
          n += (digit * (ord(string[i]) - ord('0')))
          digit *= 10
          i -= 1
        return n

      def convert_str(integer):
        s = ""
        while integer > 0:
          s += chr(integer % 10 + ord('0'))
          integer //= 10
        if s == "":
          return "0"
        else:
          return s[::-1]

      return convert_str(convert_int(num1) * convert_int(num2))
