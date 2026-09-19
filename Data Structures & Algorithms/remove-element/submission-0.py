class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 #why: this is the pointer a the beginning of the list 
        for i in range(len(nums)): # we then go throuh the array to look for 
            if nums[i] != val: # onece we find a value that is not the one we look for we make the beginign of the list that value so the list is onyl values without the value
                nums[k] = nums[i]
                k+=1
        return k
        