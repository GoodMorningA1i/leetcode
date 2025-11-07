# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        """
        Even vs Odd Length for Linked List

        1. Slow and fast pointer, this will give you a starting point for the 
        second half of the list which I can reverse
        2. Reverse the second half of the list
        3. Do arithmetic between first node in first half and reversed second half
        """

        #Step 1
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print("True 1")
        
        #Step 2
        secondHalf = slow.next

        slow.next = None #Set the end of the first half of the linked list
        
        prev = None
        curr = secondHalf
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        reversedSecondHalf = prev

        #Step3
        list1 = head
        list2 = reversedSecondHalf
        while list1 != None and list2 != None:
            temp1 = list1.next
            list1.next = list2
            list1 = temp1

            temp2 = list2.next
            list2.next = list1
            list2 = temp2