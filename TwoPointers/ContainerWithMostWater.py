class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_value = 0

        i = 0
        j = len(height) - 1
        while j > i:
            
            area = (j-i) * min (height[i], height[j])
            if area > max_value :
                max_value = area

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        
        return max_value