class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Take the shortest string in the list as common
        common = min(strs, key=len)
        
        for string in strs:
            while common != "":
            
                # If the commone match from start, go to next string in the list
                if common in string[0:len(common)]:
                    break
                
                # Otherwise, reduce until it matches or reduces to ""
                else: 
                    common = common[:-1]
        
        return common
