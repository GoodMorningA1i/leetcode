/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var neighbors: [Node?]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.neighbors = []
 *     }
 * }
 */

class Solution {
    func cloneGraph(_ node: Node?) -> Node? {
        var oldToNew: [Node: Node] = [:]

        func clone(_ node: Node?) -> Node? {
            guard let node = node else { return nil }

            if let newNode = oldToNew[node] {
                return newNode
            }
            var copy = Node(node.val)
            oldToNew[node] = copy
            for neighbour in node.neighbors {
                copy.neighbors.append(clone(neighbour))
            }

            return copy
        }

        return clone(node)
    }
}