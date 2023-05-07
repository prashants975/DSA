class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        strs_sorted = [''.join(sorted(s)) for s in strs]

        strs_both = zip(strs_sorted, strs)

        str_map={}
        for s_sort, s in strs_both:
            #print(s_sort)
            if s_sort in str_map:
                str_map[s_sort].append(s)
            else:
                str_map[s_sort] = [s]

        
        return list(str_map.values())

