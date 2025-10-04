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
    func reorderList(_ head: ListNode?) {
        //slow x1 and fast pointer x2
        //then from slow + 1, reverse and cut the first half off from the second
        //then have a reference both and do your pointer switching technique


        var slow = head
        var fast = head
        while let s = slow, let f = fast, let _ = fast?.next {
            slow = s.next
            fast = f.next?.next
        }

        var endOfFirstHalf = slow
        var startOfSecondHalf = slow?.next
        endOfFirstHalf?.next = nil

        var prev: ListNode? = nil
        var curr = startOfSecondHalf
        while let node = curr {
            var temp = node.next
            node.next = prev
            prev = node
            curr = temp
        }

        var first = head
        var second = prev

        while let node1 = first, let node2 = second {
            var temp = node1.next
            node1.next = second
            first = node1.next

            var temp2 = node2.next
            node2.next = temp
            second = node2.next
            first?.next = temp2
        }
    }
}