class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        
        if s == "":
            return 0
        #print(s)

        sign = +1 

        
        if s[0] == '+':
            sign = +1 
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]
        else:
            sign = +1

        #remove non numeric
        for i in range(len(s)):
            if not s[i].isnumeric():
                s = s[:i]
                break

        final_num = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            num = s[i]
  
            final_num = final_num + int(num) * (10 ** (n - i -1))
            #print("Number:", final_num)

            if final_num *sign <= -2**31:
                return -2**31
            if final_num *sign >= 2**31 - 1:
                return 2**31 -1
        
        return final_num * sign



            
