class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        left_c = n
        right_c = n
        final_list = []

        def generate(left_c, right_c, var):

            if right_c == left_c == 0:
                # print(left_c,right_c, var)
                final_list.append(var)
                return None

            # print(left_c, var)
            if left_c > 0:
                var_l = var + "("
                generate(left_c-1, right_c, var_l)
            
            if right_c > left_c:
                var_r = var + ")"
                generate(left_c, right_c-1, var_r)

        generate(left_c-1, right_c, "(")
        return final_list
                
