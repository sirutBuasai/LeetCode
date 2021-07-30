class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle:
            if needle in haystack:
                return haystack.index(needle)
                
            else:
                return -1
            
        else:
            return 0
          
