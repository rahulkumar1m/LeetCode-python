# Time: O(1)
# Space = O(1)


# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

from math import sqrt

class Solution:
    def __init__(self):
        self.sqrt_5 = sqrt(5)
        self.l1 = (1 + self.sqrt_5)/2
        self.l2 = (1 - self.sqrt_5)/2
        
    def fib(self, n: int) -> int:
        return int((self.l1**n-self.l2**n)/self.sqrt_5)
