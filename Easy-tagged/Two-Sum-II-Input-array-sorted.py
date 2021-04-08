# Time: O(N)
# Space: O(1)



# Given an array of integers numbers that is already sorted in ascending order
# find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer
# of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# You may assume that each input would have exactly one solution and you may 
# not use the same element twice.

class Solution:
    def twoSum(self, numbers, target: int):
        start, end = 0, len(numbers)-1
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start+1, end+1]
        
        return []
