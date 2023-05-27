class Solution:
    def isValid(self, s: str) -> bool:

        stack  = []
        char_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                pop_char = stack.pop()
                #print(pop_char, stack)
                if char_map[pop_char] != char:
                    return False
        
        if len(stack) != 0:
            return False
        return True

