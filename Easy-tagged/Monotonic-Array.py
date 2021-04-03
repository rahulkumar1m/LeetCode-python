# Time: O(n)
# Space: O(1)

class Solution:
    def isMonotonic(A: list) -> bool:
        incr = decr = True
        
        for i in range(0, len(A) - 1):
            if A[i] > A[i+1]:
                incr = False
            if A[i] < A[i+1]:
                decr = False
        
        return incr or decr
