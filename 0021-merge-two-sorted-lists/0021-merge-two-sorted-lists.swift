/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        """
        Test cases
        Sorted
        Empty, how long can they be
        Duplicates
        Same length for both linked lists, no

        124
           ^
        curr1
        
        
        134
           ^
        curr2

        """

        var result = ListNode()
        var currResult = result

        var curr1 = list1
        var curr2 = list2
        while curr1 != nil && curr2 != nil {

            var node = ListNode()

            if curr1!.val < curr2!.val {
                node.val = curr1!.val
                curr1 = curr1!.next
            } else {
                node.val = curr2!.val
                curr2 = curr2!.next
            }

            currResult.next = node
            currResult = currResult.next!
        }

        //If curr1 still has elements
        while curr1 != nil {
            var node = ListNode()
            node.val = curr1!.val
            curr1 = curr1!.next

            currResult.next = node
            currResult = currResult.next!
        }

        //If curr2 still has elements
        while curr2 != nil {
            var node = ListNode()
            node.val = curr2!.val
            curr2 = curr2!.next

            currResult.next = node
            currResult = currResult.next!
        }

        return result.next

    }
}