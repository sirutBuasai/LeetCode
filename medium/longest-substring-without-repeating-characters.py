class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        d = {}
        current_start = 0
        current_len = 0
        ans = 0
        
        for i, char in enumerate(s):
            
            # The char is already in the dict and is at later index of the current_start
            if char in d and d[char] >= current_start:
                # We restart the counting from the char after the duplicated char. (abcafedb: once a is duplicated we start again from b)
                current_start = d[char] + 1
                # Current length is current_char index - duplciated_char index
                current_len = i - d[char]
                d[char] = i
            else:
                d[char] = i
                current_len += 1
                if current_len > ans:
                    ans = current_len
        return ans
      
