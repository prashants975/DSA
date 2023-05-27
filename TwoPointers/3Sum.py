class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        #set_nums = set(nums)

        n =  len(nums)
        final_list = []

        for k in range(n-2):

            i = k+1
            j = n-1

            if k > 0 and nums[k] == nums[k-1]: #for duplicates
                continue
             
            while j > i:
                sum_ij = nums[i]+ nums[j] 
                if sum_ij + nums[k] == 0:
                    #print([nums[i], nums[j], nums[k]])
                    final_list.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1 #for duplicates
                elif nums[k] + sum_ij > 0:
                    j -= 1
                else:
                    i += 1
        
        return final_list