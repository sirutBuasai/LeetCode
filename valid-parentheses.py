class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_dict = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        stack = []
        
        for char in s:
            if char in valid_dict.values():
                stack.append(char)
                
            elif char in valid_dict.keys():
                # False if string has no corresponding open in the stack
                if stack == [] or valid_dict[char] != stack.pop():
                    return False
                
            else:
                return False
            
        return stack == []
        
