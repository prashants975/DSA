class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)

        stack = []
        stack.append(intervals[0])
        n = len(intervals)

        for i in range(1,n):
            
            last_interval = stack[-1]
            cur_interval = intervals[i]

            if last_interval[0] <= cur_interval[0] <= last_interval[1]:
                #now update the end if its larger then the last stack interval
                stack[-1][1] = max(cur_interval[1], last_interval[1])
            else:
                stack.append(cur_interval)
        
        return stack