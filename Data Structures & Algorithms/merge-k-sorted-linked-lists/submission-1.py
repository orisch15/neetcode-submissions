# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #we will start at 1 and merge i and i-1
        if len(lists) ==1:
            return lists[0]
        elif len(lists) == 0:
            return None
        return self.rec_merge(lists, 0, len(lists) - 1)
    
    def rec_merge (self, lists: List[Optional[ListNode]], l, r):
        if l>r:
            return None
        elif l == r: 
            return lists[l]
        mid = (l+r)//2

        left = self.rec_merge(lists, l, mid)
        #the mid+1 is crucial!!!!
        right = self.rec_merge(lists, mid + 1, r)

        return self.merage2list(left, right)


    def merage2list(self, lst1, lst2):
        dummy = ListNode(0)
        tail = dummy
        while lst1 and lst2:
            if lst1.val <= lst2.val:
                tail.next = lst1
                lst1 = lst1.next
            else:
                tail.next = lst2
                lst2 = lst2.next
            tail = tail.next
        tail.next = lst1 or lst2

        return dummy.next
