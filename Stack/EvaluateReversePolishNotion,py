class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack : List[int] = []
        
        n = len(tokens)
        i = 0
        while i < n:
            if tokens[i] in ['+', '-', '*', '/']:
                numb = stack.pop()
                numa = stack.pop()

                if tokens[i] == '+':
                    res = numa + numb
                elif tokens[i] == '-':
                    res = numa - numb
                elif tokens[i] == '/':
                    res = numa / numb
                else:
                    res = numa * numb

                stack.append(int(res))
            else:
                stack.append(int(tokens[i]))

            i += 1


        return int(stack.pop())

