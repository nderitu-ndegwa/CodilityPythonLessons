
"""


For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

    val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function:

    def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

For example, given array:
  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2

your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..20,000];
        each element of array A is an integer within the range [−100..100].


"""

def solution(A):
    # Sort the array in non-decreasing order
    A.sort()

    # Initialize pointers and min_sum
    left = 0
    right = len(A) - 1
    min_sum = 10**9

    # Loop through the array
    while left <= right:
        # Compute the sum of the elements at the left and right pointers
        # multiplied by -1 and 1, respectively
        curr_sum = -A[left] + A[right]

        # Update min_sum if necessary
        if abs(curr_sum) < min_sum:
            min_sum = abs(curr_sum)

        # Move the pointers
        if curr_sum < 0:
            left += 1
        else:
            right -= 1

    return min_sum
