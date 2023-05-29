class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []#[temperatures[0]]
        final_res = [0]*len(temperatures)
            
        for i in range(0,len(temperatures)):

            while (stack):
                if temperatures[i] > stack[-1][0]:
                    s_temp, s_idx = stack.pop()
                    # print(i, s_temp, s_idx)
                    final_res[s_idx] = (i - s_idx)
                else:
                    break
            
            stack.append([temperatures[i], i])

            


        return final_res