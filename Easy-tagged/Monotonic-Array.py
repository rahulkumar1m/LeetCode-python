# Time: O(n)
# Space: O(1)


# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

class Solution:
    def isMonotonic(A: list) -> bool:
        incr = decr = True
        
        for i in range(0, len(A) - 1):
            if A[i] > A[i+1]:
                incr = False
            if A[i] < A[i+1]:
                decr = False
        
        return incr or decr
