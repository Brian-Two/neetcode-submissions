class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currThres = 0
        count = 0
        l = 0
        target = threshold * k
        for r in range(len(arr)):
            currThres += arr[r]
            if r-l+1 == k:
                if currThres >= target:
                    count +=1
                currThres -= arr[l]
                l+=1
            

        return count 

      