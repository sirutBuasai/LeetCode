class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      h_len = len(haystack)
      n_len = len(needle)
      
      if not needle:
        return 0
      
      if n_len > h_len:
        return -1
      
      else:
        for i in range(h_len-n_len+1):
          if haystack[i:i+n_len] == needle:
            return i
          
        return -1
      
