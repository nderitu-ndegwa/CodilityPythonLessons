'''
Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

'''

def solution(A, B, K):
    # Count of integers divisible by K in the range [0..B]
    count_B = B // K

    # Count of integers divisible by K in the range [0..A-1]
    count_A = (A - 1) // K if A > 0 else 0

    # Return the count of integers divisible by K in the range [A..B]
    return count_B - count_A

# Compare this snippet from Codility/GenomicRangeQuery.py:
