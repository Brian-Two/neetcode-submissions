class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {'}':'{', ']':'[', ')':'('}

        for char in s:

            if char in '[{(':
                stack.append(char)
            else:
                if stack == [] or stack[-1] != paren[char]:
                    return False 
                else:
                   stack.pop()

        
        return True if stack == [] else False
