class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if nums == []:
        #     return 
        set_nums = set(nums)
        count_max = 0

        for n in set_nums:
            if n-1 not in set_nums:  #it is the start of the sequence
                ele = n
                count = 0
                
                while ele in set_nums:
                    count += 1
                    ele += 1
                
                #print("start,end: ", n , ele - 1, count)

                if count_max < count:
                    count_max = count
                   
        return count_max