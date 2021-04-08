# Time: O(N^2)
# Space: O(1)


# Given an array of integers nums and an integer target, return indices of 
# the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.


class Solution1:
    def twoSum(self, nums, target: int):
        # Looping through all elements in the list to check for 
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

class Solution2:
    def twoSum(self, nums, target: int):
        h = {}
        # Looping through all elements in the list to check for 
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[num], i]
        
        return []
