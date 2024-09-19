class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        punctuation = '''!()-[]{};:'"`\, <>./?@#$%^&*_~'''
        l = 0
        r = len(s)-1
        while l < r:
          while s[l] in punctuation and l < r:
            l += 1

          while s[r] in punctuation and l < r:
            r -= 1

          if s[l] != s[r]:
            return False

          else:
            l += 1
            r -= 1

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
          while not s[l].isalnum() and l < r:
            l += 1
          while not s[r].isalnum() and l < r:
            r -= 1

          if s[l] != s[r]:
            return False
          else:
            l += 1
            r -= 1

        return True
