class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'}':'{', ']':'[', ')':'('}
        stack = []

        for paren in s:

            if paren in (list(parens.values())):
                stack.append(paren)
            elif paren in paren:
                if not stack or stack.pop() != parens[paren]:
                    return False
            
        return True if not stack else False
        