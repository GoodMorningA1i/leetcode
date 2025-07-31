class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        result = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            result[sorted_str].append(s)

        return list(result.values())

       #Time Complexity: O(m*nlogn)
       #Space Complexity: O(m*n)
        
