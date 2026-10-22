# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr, p = dummy, head
        #advance p n steps so when it will reach the end curr will be n+1 places from the end
        for _ in range(n):
            p = p.next
        while p:
            p = p.next
            curr = curr.next
        #now curr is one step before the designated node - lets pass it
        curr.next = curr.next.next

        return dummy.next
