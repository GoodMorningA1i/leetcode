class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        d = defaultdict(int)
        for l in lights:
            low = l[0] - l[1]
            high = l[0] + l[1]
            #print(low, high)
            d[low] += 1
            d[high + 1] -= 1

        d = dict(sorted(d.items(), key=lambda x: x[0]))
        #print(d)
        d_summed = list(itertools.accumulate(d.values()))
        #print(d_summed)

        biggest = max(d_summed)
        keysList = list(d.keys())
        for i, k in enumerate(keysList):
            if d_summed[i] == biggest:
                return k