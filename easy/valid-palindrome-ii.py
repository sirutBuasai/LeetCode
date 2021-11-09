class Solution:
    def validPalindrome(self, s: str) -> bool:
        def skip_idx(string, i):
          left = 0
          right = len(string)-1
          
          while left < right:
            if left == i:
              left += 1
              continue
            
            if right == i:
              right -= 1
              continue
              
            if string[left] != string[right]:
              return False
            else:
              left += 1
              right -= 1
          return True
              
        l = 0
        r = len(s)-1
        while l < r:
          if s[l] != s[r]:
            return skip_idx(s, l) or skip_idx(s, r)
          else:
            l += 1
            r -= 1
        return True
        
