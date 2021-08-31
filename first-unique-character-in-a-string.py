class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for i, c in enumerate(s):
          if c not in d.keys():
            d[c] = i
          else:
            d[c] = -1
            
        for k in d.keys():
          if d[k] != -1:
            return d[k]

        return -1
      
