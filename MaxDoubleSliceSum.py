def solution(A):
    N = len(A)
    max_ending = [0] * N
    max_starting = [0] * N
    
    for i in range(1, N-1):
        max_ending[i] = max(max_ending[i-1] + A[i], 0)
        max_starting[N-i-1] = max(max_starting[N-i] + A[N-i-1], 0)
    
    max_double_slice_sum = 0
    
    for i in range(1, N-1):
        double_slice_sum = max_ending[i-1] + max_starting[i+1]
        max_double_slice_sum = max(max_double_slice_sum, double_slice_sum)
    
    return max_double_slice_sum
