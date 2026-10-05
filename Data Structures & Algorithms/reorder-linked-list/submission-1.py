# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we first want to fidn the middle of the list and split it so we can work with bit halves
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        first, second = head, slow.next 
        slow.next = None

        # now that we have two hlaves; ex: [2,4,6,8] frist: [2,4], second:[6,8] we want to reverse the second one

        #reverse second list 
        prev = None
        while second:
            temp = second.next 
            second.next = prev
            prev = second
            second = temp
        second = prev # prev is not th head of the list 
        #now that second: [8,6] we want to merge the two list 

        # merge first and second 
        while first and second:
            # use temp values since we are changign next place
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1

            # my issure is on how to upcade this
            first = tmp1
            second = tmp2


        
        


            

