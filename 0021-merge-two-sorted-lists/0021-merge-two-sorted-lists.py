# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        while loop
        whichever one is greater, add that one first

        after while loop,
        check both linked list to see if there are any elements left
        and append them

        Is there more optimal way to do this? Nope, this is all I can find
        """
        curr1 = list1
        curr2 = list2
        res = ListNode()
        curr = res

        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        
        curr.next = curr1 if curr1 else curr2

        return res.next
