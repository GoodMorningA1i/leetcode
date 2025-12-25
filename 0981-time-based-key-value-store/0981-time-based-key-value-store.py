from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) #key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int):
        self.map[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map[key]

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res