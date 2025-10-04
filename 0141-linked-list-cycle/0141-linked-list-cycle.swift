/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        var s = head
        var f = head
        while f != nil && f?.next != nil {
            s = s?.next
            f = f?.next?.next

            if s === f {
                return true
            }
        }

        return false
    }
}
