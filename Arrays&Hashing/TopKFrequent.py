class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:

            if n not in count:
                count[n] = 0
            else:
                count[n] += 1
        
        counts_list = sorted(count.items(), key= lambda x: x[1], reverse = True)[:k]

        return [k for k,v in counts_list]


        