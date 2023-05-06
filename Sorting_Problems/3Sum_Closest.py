class Solution:
    import sys
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        n = len(nums)

        if n == 3:
            return sum(nums)
        closestSum = sys.maxsize

        # -2  as we will select two more pointers
        for i in range(n- 2):
            
            p1 = i+1 #left pointer
            p2 = n-1 #right pointer

            while(p1 < p2):
                
                tri_sum = nums[i] + nums[p1] + nums[p2]

                if abs(target - tri_sum) < abs(target - closestSum):
                    closestSum = tri_sum

                if tri_sum > target:
                    p2 = p2 - 1
                elif tri_sum < target:
                    p1 = p1 + 1
                else:
                    return target
            

        return closestSum





        
        