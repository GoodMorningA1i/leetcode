//ChatGPT, thank you

class Node {
    var key: Int
    var value: Int
    var prev: Node?
    var next: Node?

    init(_ key: Int = 0, _ value: Int = 0) {
        self.key = key
        self.value = value
    }
}

class LRUCache {
    private let capacity: Int
    private var cache = [Int: Node]()
    private let head = Node()
    private let tail = Node()

    init(_ capacity: Int) {
        self.capacity = capacity
        head.next = tail
        tail.prev = head
    }

    private func remove(_ node: Node) {
        let prev = node.prev
        let next = node.next
        prev?.next = next
        next?.prev = prev
    }

    private func insertAtTail(_ node: Node) {
        let prev = tail.prev
        prev?.next = node
        node.prev = prev
        node.next = tail
        tail.prev = node
    }

    func get(_ key: Int) -> Int {
        guard let node = cache[key] else { return -1 }
        remove(node)
        insertAtTail(node)
        return node.value
    }

    func put(_ key: Int, _ value: Int) {
        if let node = cache[key] {
            node.value = value
            remove(node)
            insertAtTail(node)
        } else {
            if cache.count >= capacity, let lru = head.next, lru !== tail {
                remove(lru)
                cache.removeValue(forKey: lru.key)
            }

            let newNode = Node(key, value)
            cache[key] = newNode
            insertAtTail(newNode)
        }
    }
}
