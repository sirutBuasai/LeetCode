class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def check_rotation(string, p2, goal_string):
          p1 = 0
          while p1 < len(goal_string):
            if goal_string[p1] != string[p2]:
              return False
            p1 += 1
            p2 = (p2+1) % len(string)
          return True
      
        if len(s) != len(goal):
          return False
                
        for i in range(len(s)):
          if s[i] == goal[0] and check_rotation(s, i, goal):
            return True
            
        return False
