class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      
      d_p = {}
      ans = []
        
      for p in points:
        dist = (p[0]*p[0]) + (p[1]*p[1])
        if dist in d_p.keys():
          d_p[dist] += [p]
          
        else:
          d_p[dist] = [p]
          
      for d in sorted(d_p.keys()):
        if len(ans) < k:
          ans += d_p[d]
          
      return ans
        
