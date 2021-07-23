class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        d = {}
        current_start = 0
        current_len = 0
        ans = 0
        
        for i, char in enumerate(s):
            if char in d and d[char] >= current_start:
                current_start = d[char] + 1
                current_len = i - d[char]
                d[char] = i
            else:
                d[char] = i
                current_len += 1
                if current_len > ans:
                    ans = current_len
        return ans
      
