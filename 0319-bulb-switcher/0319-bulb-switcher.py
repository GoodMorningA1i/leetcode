class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        n = 5
        [off, off, off, off, off]
        Round 1: [on, on, on, on, on]
        Round 2: [on, off, on, off, on]
        Round 3: [on, off, off, off, on]
        Round 4: [on, off, off, on, on]
        Round 5: [on, off, off, on, off]

        n = 8
        [off, off, off, off, off, off, off, off]
        Round 1: [on, on, on, on, on, on, on, on]
        Round 2: [on, off, on, off, on, off, on, off]
        Round 3: [on, off, off, off, on, on, on, off]
        Round 4: [on, off, off, on, on, on, on, on]
        Round 5: [on, off, off, on, off, on, on, on]
        Round 6: [on, off, off, on, off, off, on, on]
        Round 7: [on, off, off, on, off, off, off, on]
        Round 8: [on, off, off, on, off, off, off, off]
        ^
        |
        [on, off, off, on, on, on, on, on]
                        ^  

        O(n^(n//2))
        """
        return int(sqrt(n))