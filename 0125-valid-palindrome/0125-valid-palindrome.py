"""
ata
true

atta
true


ate, eta
true

hello, bob
false

ate, eat
false

ate, ETA
true

ate, ETA_%#@
true

Test cases
empty

Start from the beginning
Start from the end
See if they make the same work
O(2n) = O(n)
O(n)

pointer at start
pointer at end
see if they match
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = ""
        for char in s:
            if char.isalnum():
                alnum_s += char

        pointerA = 0
        pointerB = len(alnum_s) - 1
        while pointerA < pointerB:
            if alnum_s[pointerA].lower() != alnum_s[pointerB].lower():
                return False
            pointerA += 1
            pointerB -= 1
        return True