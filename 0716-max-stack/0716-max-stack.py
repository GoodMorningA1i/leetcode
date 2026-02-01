class MaxStack:
    def __init__(self):
        self.stack = SortedList() #(id, val) sorted by id 
        self.values = SortedList() #(val, id) sorted by val
        self.count = 0

    def push(self, x):
        self.stack.add((self.count, x))
        self.values.add((x, self.count))
        self.count += 1
    
    def pop(self) -> int:
        index, val = self.stack.pop()
        self.values.remove((val, index))
        return val
    
    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        val, index = self.values.pop()
        self.stack.remove((index, val))
        return val


"""
element storing in a particular order
LIFO

[1,5,6]


Let n be the number of elements in the stack

[6, 1, 5]

6, (index)
| |
1 5

"""