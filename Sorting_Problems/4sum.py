class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        quad_sum_list = set()
        for i in range(n - 3):
            for j in range(i+1, n - 2):
                p1 = j + 1
                p2 = n - 1

                while (p1 < p2):
                    quad_sum = nums[i] + nums[j] + nums[p1] + nums[p2]

                    if quad_sum == target:
                        quad_sum_list.add((nums[i], nums[j], nums[p1], nums[p2]))

                    if quad_sum <= target:
                        p1 += 1
                    else:
                        p2 -= 1

        return list(quad_sum_list)