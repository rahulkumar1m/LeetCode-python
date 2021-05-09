# Time: O(N^2)
# Space: O(N)

# One of the test cases is wrong

# Given a string S of digits, such as S = "123456579", we can split it into a 
# Fibonacci-like sequence [123, 456, 579].

# Formally, a Fibonacci-like sequence is a list F of non-negative integers such 
# that:

#     0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
#  type);
#     F.length >= 3;
#     and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

# Also, note that when splitting the string into pieces, each piece must not 
# have extra leading zeroes, except if the piece is the number 0 itself.

# Return any Fibonacci-like sequence split from S, or return [] if it cannot be 
# done.

from typing import List
import sys

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        # Initialize a vector to store sequence
        seq = []

        # Call the helper function
        self.splitIntoFibonacciHelper(0, S, seq)

        if len(seq) > 2:
            return seq
        else:
            return []
    
    def splitIntoFibonacciHelper(self, pos, S, seq):
        if (pos == len(S)) and (len(seq) >= 3):
            return True
        
        num = 0

        for i in range(pos, len(S)):
            num = num * 10 + (ord(S[i]) - ord('0'))

            # Avoid integer overflow 
            if (num > sys.maxsize):
                break
            
            # Avoid leading zeros
            if (ord(S[pos]) == ord('0') and i > pos):
                break
            
            # If the current number is greater than last two number of seq
            if (len(seq) > 2 and (num > (seq[-1] + seq[len(seq) - 2]))):
                break
            
            # If seq length is less 2 or current number is equal to the last two od the seq
            if (len(seq) < 2 or (num == (seq[-1] + seq[len(seq) - 2]))):
                # Add to the seq
                seq.append(num)

                # Recur for i + 1
                if self.splitIntoFibonacciHelper(i+1, S, seq):
                    return True
                
                # Remove last added number
                seq.pop()

        # If no sequence is found
        return False
