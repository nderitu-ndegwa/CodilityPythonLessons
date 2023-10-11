def solution(A):
    max_ending_here = max_so_far = A[0]
    for a in A[1:]:
        max_ending_here = max(a, max_ending_here + a)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
