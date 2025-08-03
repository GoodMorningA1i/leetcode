class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointerA = 0
        pointerB = len(numbers) - 1

        while pointerA < pointerB:
            if numbers[pointerA] + numbers[pointerB] < target:
                pointerA += 1
            elif numbers[pointerA] + numbers[pointerB] > target:
                pointerB -= 1
            else:
                break

        return [pointerA + 1, pointerB + 1]
