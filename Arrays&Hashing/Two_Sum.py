class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_pairs = {}

        for i in range(len(nums)):
            
            diff = target - nums[i]
            if nums[i] in sum_pairs:
                return [sum_pairs[nums[i]], i]
            else:
                sum_pairs[diff] = i

        return []