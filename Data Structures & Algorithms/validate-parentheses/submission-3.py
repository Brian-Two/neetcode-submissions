class Solution:
    def isValid(self, s: str) -> bool:
        closed_open = {')':'(', ']':'[', ')':'(','}':'{'}
        open_brackets = ('(', '[', '{')
        stack = []
        # "["
        for letter in s:
            if letter in open_brackets:
                stack.append(letter)
            else:
                if not stack or stack[-1] != closed_open[letter]:
                    return False
                else:
                    stack.pop()
        
        return True if stack == [] else False
                