class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tOccurences = {}
        for char in t:
            if char not in tOccurences:
                tOccurences[char] = 0
            tOccurences[char] += 1
        
        sWindowOccurences = {}
        res = [-1, -1]
        resLen = float("infinity")
        have, need = 0, len(tOccurences)
        l = 0

        for r in range(len(s)):
            char = s[r]

            if char not in sWindowOccurences:
                sWindowOccurences[char] = 0
            sWindowOccurences[char] += 1

            if char in tOccurences and sWindowOccurences[char] == tOccurences[char]:
                have += 1
            
            while have == need:
                #update our result
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                #pop from the left
                sWindowOccurences[s[l]] -= 1
                if s[l] in tOccurences and sWindowOccurences[s[l]] < tOccurences[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
                    

