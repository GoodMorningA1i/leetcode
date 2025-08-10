class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        
        if digits[index] != 9:
            digits[-1] += 1
        else:
            while index >= 0:
                if digits[index] == 9:
                    digits[index] = 0
                    index -= 1
                    if index < 0:
                        digits.insert(0, 1)
                else:
                    digits[index] += 1
                    break
        
        return digits