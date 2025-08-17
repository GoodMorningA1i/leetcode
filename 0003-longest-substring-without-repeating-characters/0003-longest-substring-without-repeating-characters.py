class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1

        if len(s) == 0 or len(s) == 1:
            return len(s)

        for left in range(len(s)):
            duplicate_found = False
            for right in range(left + 1, len(s)):
                for k in range(left, right):
                    if s[right] == s[k]:
                        duplicate_found = True
                        break
                if duplicate_found:
                    break
                else:
                    longest = max(longest, right - left + 1)
        
        return longest