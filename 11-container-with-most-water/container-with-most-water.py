class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Area = width * min height
            current = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current)
            
            # Move shorter pointer (area can't increase otherwise)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
        