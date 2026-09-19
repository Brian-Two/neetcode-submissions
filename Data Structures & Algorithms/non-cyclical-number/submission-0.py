class Solution:
    def isHappy(self, n: int) -> bool:
        seen  = set()

        while n not in seen:
            curr = 0 
            for num in str(n):
                curr += int(num)**2
            if curr == 1:
                return True
            seen.add(n)
            n = curr        



        return False


            