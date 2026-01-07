class DoubleLinkedList:
    def __init__(self, key=0, value=0, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DoubleLinkedList(key, value)
            self.insert(node)
            self.cache[key] = node
        else:
            self.cache[key].value = value
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

        if len(self.cache) > self.capacity:
            #Remove LRU
            del self.cache[self.head.nxt.key]
            self.remove(self.head.nxt)

    def remove(self, node):
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt

    def insert(self, node):
        temp = self.tail.prev
        self.tail.prev = node
        node.nxt = self.tail
        
        node.prev = temp
        temp.nxt = node
