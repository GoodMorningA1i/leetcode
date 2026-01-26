class TimeMap:
    def __init__(self):
        self.map = defaultdict(list) #list elements will be (value, timestamp)
    
    def set(self, key, value, timestamp):
        self.map[key].append((value, timestamp))
    
    def get(self, key, timestamp):
        values = self.map[key]

        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res