class RandomizedSet:
    def __init__(self):
        self.set = set()

    def insert(self, val):
        if val in self.set:
            return False
        self.set.add(val)
        return True
    
    def remove(self, val):
        if val not in self.set:
            return False
        self.set.remove(val)
        return True
    
    def getRandom(self):
        setArr = list(self.set)
        length = len(setArr)
        randomIndex = random.randint(0, length - 1)
        return setArr[randomIndex]
