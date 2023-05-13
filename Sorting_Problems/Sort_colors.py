class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0, 0] #0,1,2
        for n in nums:
            counts[n] += 1
        print(counts)

        k = 0
        final = [0]*counts[0] + [1]*counts[1] + [2]*counts[2]
        for i in range(len(final)):
            nums[i] = final[i]
            


