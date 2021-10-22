class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def build_string(result_list, curr, open_p, close_p, max_p):
          if len(curr) == (max_p*2):
            result_list.append(curr)
            
          if open_p < max_p:
            build_string(result_list, curr+'(', open_p+1, close_p, max_p)
            
          if close_p < open_p:
            build_string(result_list, curr+')', open_p, close_p+1, max_p)
            
        result = []
        build_string(result, "", 0, 0, n)
        return result
        
