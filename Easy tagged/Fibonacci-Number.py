from math import sqrt

class Solution:
    def __init__(self):
        self.sqrt_5 = sqrt(5)
        self.l1 = (1 + self.sqrt_5)/2
        self.l2 = (1 - self.sqrt_5)/2
        
    def fib(self, n: int) -> int:
        return int((self.l1**n-self.l2**n)/self.sqrt_5)
