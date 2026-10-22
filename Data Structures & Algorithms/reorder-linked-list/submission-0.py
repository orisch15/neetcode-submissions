# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        slow, fast = head, head.next
        #to make sec go to the n\\2 - 1 index
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #now second is the beggining of the second half
        #slow.next is none so we would have two separate halfs
        second = slow.next
        slow.next = None

        #reverse second list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 
        #now prev is the new head so
        second = prev
        #begin the marge

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2











