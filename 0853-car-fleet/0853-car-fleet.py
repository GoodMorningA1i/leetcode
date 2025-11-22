class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Brute force:

        0,1,2,3,4,5,6,7,8,9,10,11,12
        3 3
              5     5
                  4 4    
                        2          2 
                             1     1
        

        Fleet
        (1,2)
        (4,5)
        (3)

        Time Complexity: O(n * speed(n))
        Space Complexity: O(target)


        """
        
        pairs = []
        n = len(position)
        for i in range(n):
            pairs.append([position[i], speed[i]])
        
        pairsSorted = sorted(pairs, key=lambda x: x[0])
        stack = []

        while len(pairsSorted) > 0:
            p,s = pairsSorted.pop()
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
