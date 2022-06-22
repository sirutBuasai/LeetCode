class Solution:
    def myAtoi(self, s: str) -> int:
      def clean(string):
        cleaned = ""
        for c in string:
          if not cleaned:
            if c.isdigit() or c == '-' or c == '+':
              cleaned += c
            elif c == ' ':
              continue
            else:
              return cleaned
          else:
            if c.isdigit():
              cleaned += c
            else:
              return cleaned

        return cleaned

      def clamp(num):
        if num > ((2**31)-1):
          return ((2**31)-1)
        elif num < (-2**31):
          return (-2**31)
        else:
          return num

      def convert(string):
        num = 0
        mult = 10**(len(string)-1)
        while string:
          digit = ord(string[0]) - ord('0')
          num += (mult*digit)
          mult //= 10
          string = string[1:]

        return num

      s = clean(s)
      if not s:
        return 0

      if s[0] == '-':
        return clamp(convert(s[1:])*-1)
      elif s[0] == "+":
        return clamp(convert(s[1:]))
      else:
        return clamp(convert(s))
