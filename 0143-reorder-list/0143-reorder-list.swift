"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Linked List
[1,2,3,4,5,6,7] -> null
^
       ^      ^

[1,2,3,4] -> null
^

7 -> 6 -> 5
[7,6,5]
^

3 -> 2 -> 1


[1, 7]
[1,7,2,6,3,5,4]


1) Get the length of linked list
2) Go to the middle of linked list
3) We have a pointer at the start

[1, 1000]
linked list has at least 1 node



"""

// class ListNode {
//     public var val: Int
//     public var next: ListNode?
//     public init(val: Int = 0, next: ListNode? = nil) {
//         self.val = val
//         self.next = next
//     }
// }

class Solution {
    func reorderList(_ head: ListNode?) -> ListNode? {
        """
        [1,2,3,4,5,6,7]
        2 -> 1

        1 -> 2
        temp = 2 -> 3 -> ...
        1 -> nil
        temp.next = 1

        2 -> 1
        3
        3 -> 2 -> 1

        """

        var curr = head
        var arr: [ListNode?] = []
        while let node = curr {
            arr.append(node)
            curr = node.next
        }
        
        var result = ListNode()
        var currResult: ListNode? = result
        var l = 0
        var r = arr.count - 1
        while l <= r {
            currResult?.next = arr[l]
            l += 1
            currResult = currResult?.next
            print(currResult?.val)

            currResult?.next = arr[r]
            r -= 1
            currResult = currResult?.next
            print(currResult?.val)
        }

        return result.next
    }
}