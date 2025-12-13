# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.curr1 = l1
        self.curr2 = l2

        res = ListNode()
        self.newCurr = res
        self.carryOver = False

        def addTwoDigits(val1, val2):
            sum = val1 + val2
            if self.carryOver:
                sum += 1
            
            if sum >= 10:
                sum = sum % 10
                self.carryOver = True
            else:
                self.carryOver = False

            if self.curr1:
                self.curr1 = self.curr1.next
            if self.curr2:
                self.curr2 = self.curr2.next

            node = ListNode(sum)
            self.newCurr.next = node
            self.newCurr = self.newCurr.next

        while self.curr1 and self.curr2:
            addTwoDigits(self.curr1.val, self.curr2.val)
        
        while self.curr1:
            addTwoDigits(self.curr1.val, 0)
        
        while self.curr2:
            addTwoDigits(0, self.curr2.val)
    
        if self.carryOver:
            node = ListNode(1)
            self.newCurr.next = node
            self.newCurr = self.newCurr.next

        return res.next