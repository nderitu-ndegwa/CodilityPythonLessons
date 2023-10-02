'''
Task description

You are given N counters, initially set to 0, and you have two possible operations on them:

        increase(X) − counter X is increased by 1,
        max counter − all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given. This array represents consecutive operations:

        if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
        if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
    
'''

def solution(N, A):
    counter = [0] * N
    base = 0
    max_val = 0

    for operation in A:
        if operation <= N:
            if counter[operation - 1] < base:
                counter[operation - 1] = base
            counter[operation - 1] += 1
            max_val = max(max_val, counter[operation - 1])
        else:
            base = max_val
    
    for i in range(N):
        if counter[i] < base:
            counter[i] = base
    
    return counter