class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_palindrome = ""
        for c in s:
            if c.isalnum():
                converted_palindrome += c

        startPointer = 0
        endPointer = len(converted_palindrome) - 1

        while startPointer < endPointer:
            if converted_palindrome[startPointer].lower() != converted_palindrome[endPointer].lower():
                return False
            startPointer += 1
            endPointer -= 1

        return True
