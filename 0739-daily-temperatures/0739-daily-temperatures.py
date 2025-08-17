class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        monotonic_stack = [] #pair: [element, index]
        for i, t in enumerate(temperatures):
            while monotonic_stack and t > monotonic_stack[-1][0]:
                stackT, stackIndex = monotonic_stack.pop()
                answer[stackIndex] = i - stackIndex
            monotonic_stack.append((temperatures[i], i))

        return answer