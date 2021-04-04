# Time: O(Log n)
# Space: O(1)


# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# This problem is just a subset of finding n+1 th number in fibonacci series

from math import sqrt

class Solution:
    def __init__(self):
        self.sqrt_5 = sqrt(5)
        self.l1 = (1 + self.sqrt_5)/2
        self.l2 = (1 - self.sqrt_5)/2
        
    def climbStairs(self, n: int) -> int:
        n += 1
        return int((self.l1**n-self.l2**n)/self.sqrt_5)
