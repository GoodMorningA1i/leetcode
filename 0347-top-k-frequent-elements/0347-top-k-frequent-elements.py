class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def findLargestNumInDict(nums_to_occurences, nums_used):
            #Find the max in dictionary
            #Add a temp array of the occurences
            #Max cannot be in this array because it was already checked
            #Find the next max
            
            max_occurence = 0
            max_num = -10^5
            for num in nums_to_occurences:
                occurence = nums_to_occurences[num]
                if occurence > max_occurence and num not in nums_used:
                    max_occurence = occurence
                    max_num = num
            
            return max_num
            
        nums_to_occurences_dict = {}
        for num in nums:
            if num not in nums_to_occurences_dict:
                nums_to_occurences_dict[num] = 0
            nums_to_occurences_dict[num] += 1
        
        nums_used = []
        for i in range(k):
            max_num = findLargestNumInDict(nums_to_occurences_dict, nums_used)
            nums_used.append(max_num)

        return nums_used    

        #Brute force
        #Creating a dictionary of integer element with number of occurences
        #Sort?
        #Choose the top k most frequent elements
        #Time Complexity: O(n*k)
        #Space Complexity: O(n)

        #Actually same as above but different approach
        #Sliding Windows
        #Make sure it sorted
        #Increment the window, keep track of the largest ones
        #Time Complexity: O(n^2)
        #Space Complexity: O(1) -> O(n)

        #Optimal?