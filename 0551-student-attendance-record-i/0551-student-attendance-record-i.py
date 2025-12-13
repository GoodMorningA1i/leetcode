class Solution:
    def checkRecord(self, s: str) -> bool:
        numAbsences = 0
        consecutiveLates = 0
        for char in s:
            if char == 'A':
                numAbsences += 1
                consecutiveLates = 0
            elif char == 'L':
                consecutiveLates += 1
                if consecutiveLates == 3:
                    return False
            else:
                consecutiveLates = 0
        
        return numAbsences < 2
                
            
            