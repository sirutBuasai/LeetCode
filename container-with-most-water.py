class Solution:
    def maxArea(self, height: List[int]) -> int:
        lower = 0
        upper = len(height) - 1
        volume = 0
        
        while lower < upper:
            volume = max(volume, (upper - lower) * min(height[lower], height[upper]))
            if height[lower] < height[upper]:
                lower += 1
            else:
                upper -= 1
        
        return volume
        
