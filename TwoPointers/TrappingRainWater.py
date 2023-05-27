class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        lmax = height[0]
        rmax = height[n-1]

        i = 0
        j = n-1

        total = 0
        while j > i:
            
            if lmax < rmax:
                i += 1
                lmax = max(lmax, height[i])
                total += lmax - height[i]
            else:
                j -= 1
                rmax = max(rmax, height[j])
                total += rmax - height[j]
        
        return total








