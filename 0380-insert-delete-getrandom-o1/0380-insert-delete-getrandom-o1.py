"""
Implement the RandomizedCollection class:

RandomizedCollection() 
    Initializes the collection.

bool insert(int val) 
    Inserts a value into the collection. 
    Returns true if the collection did not already contain the specified element.
    Return false, don't add to collection

bool remove(int val) 
    Removes a value from the collection. 
    Returns true if the collection contained the specified element.
    Return false if it doesn't.

int getRandom() 
    Returns a random element from the current collection of elements. 
    Probability of getting each element is equal 
   

Each function must run in average O(1) time.

selected_item = random.choice(my_list)


Duplicates are not allowed
Collections have integer elements

collection = {}
Example:
    rs = RandomizedSet()
    print(rs.insert(1))   # True  (1 was not present, now inserted) {1: 0}, [1]
    print(rs.remove(2))   # False (2 not present, cannot remove) {1: 0} [1]
    print(rs.insert(2))   # True  (2 inserted) {1: 0, 2: 1} [1, 2]
    print(rs.getRandom()) # Randomly 1 or 2, each with probability 1/2 {1: 0, 2: 1} [1, 2]
    print(rs.remove(1))   # True  (1 was present and removed) {2: 0} [2]
    print(rs.insert(2))   # False (2 already present, cannot insert again) {2: 0} [2]
    print(rs.getRandom()) # Always 2, since it's the only element left {2: 0} [2]

    
    [1, 2, 3]  

"""

from collections import defaultdict
import random

class RandomizedSet:
    def __init__(self):
        self.stack = []
        self.collection = defaultdict(int)
        
    def insert(self, val: int) -> bool:
        """
        Example:
        rs = RandomizedSet()
        print(rs.insert(1))   # True  (1 was not present, now inserted) {1: 0}, [1]
        print(rs.remove(2))   # False (2 not present, cannot remove) {1: 0} [1]
        print(rs.insert(2))   # True  (2 inserted) {1: 0, 2: 1} [1, 2]
        print(rs.getRandom()) # Randomly 1 or 2, each with probability 1/2 {1: [0], 2: [2]} [1, 1, 2]
        print(rs.remove(1))   # True  (1 was present and removed) {2: 0} [2]
        print(rs.insert(2))   # False (2 already present, cannot insert again) {2: 0} [2]
        print(rs.getRandom()) # Always 2, since it's the only element left {2: 0} [2]
        """
        if val in self.collection:
            return False
        
        self.stack.append(val)
        self.collection[val] = len(self.stack) - 1 #len is guaranteed to be at least 1
        return True
    
    def remove(self, val: int) -> bool:
        """
        Example:
        rs = RandomizedSet()
        print(rs.insert(1))   # True  (1 was not present, now inserted) {1: 0}, [1]
        print(rs.remove(2))   # False (2 not present, cannot remove) {1: 0} [1]
        print(rs.insert(2))   # True  (2 inserted) {1: 0, 2: 1} [1, 2]
        print(rs.getRandom()) # Randomly 1 or 2, each with probability 1/2 {1: 0, 2: 1} [1, 2]
        -> print(rs.remove(1))   # True  (1 was present and removed) {2: 0} [2]
        print(rs.insert(2))   # False (2 already present, cannot insert again) {2: 0} [2]
        print(rs.getRandom()) # Always 2, since it's the only element left {2: 0} [2]
        """
        if val not in self.collection:
            return False
        
        tempIndex = self.collection[val] #0
        lastElement = self.stack[-1] #2
        self.collection[lastElement] = tempIndex #1
        
        temp = self.stack[tempIndex] 
        self.stack[tempIndex] = self.stack[-1] 
        self.stack[-1] = temp
        
        self.stack.pop()
        del self.collection[val]
        
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.stack)
    
# rs = RandomizedSet()
# print(rs.insert(1))   # True  (1 was not present, now inserted) {1: 0}, [1]
# print(rs.remove(2))   # False (2 not present, cannot remove) {1: 0} [1]
# print(rs.insert(2))   # True  (2 inserted) {1: 0, 2: 1} [1, 2]
# print(rs.getRandom()) # Randomly 1 or 2, each with probability 1/2 {1: 0, 2: 1} [1, 2]
# print(rs.remove(1))   # True  (1 was present and removed) {2: 0} [2]
# print(rs.insert(2))   # False (2 already present, cannot insert again) {2: 0} [2]
# print(rs.getRandom()) # Always 2, since it's the only element left {2: 0} [2]
    
    
    
    
    
    
    