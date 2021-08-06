class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        current = ""
        
        for i in range(len(s)):
          # Even palindrome
          l = i
          r = i+1
          while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
          current = s[l+1:r]
          longest = max(current, longest, key=len)
          
          # Odd palindrome
          l = i
          r = i
          while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
          current = s[l+1:r]
          longest = max(current, longest, key=len)
          
        return longest
            
