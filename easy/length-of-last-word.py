class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        
        for c in s[::-1]:
            if c != " ":
                count += 1
                
            elif c == " ":
                if count > 0:
                    break
                else:
                    continue
            
        return count
    
