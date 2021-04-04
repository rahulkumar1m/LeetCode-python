# Time: 
# Space:


# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class Solution:
    def __init__(self):
        self.index = [None]*38
        self.index[0], self.index[1], self.index[2] = 0, 1, 1

    def tribonacci(self, n: int) -> int:
        if self.index[n] is None:
            self.index[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return self.index[n]
        else:
            return self.index[n]
