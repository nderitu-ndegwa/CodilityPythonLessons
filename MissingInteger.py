def solution(A):
    A.sort()
    if A[-1] <= 0:
        return 1
    elif A[0] > 1:
        return 1
    else:
        for i in range(len(A)-1):
            if A[i] > 0 and A[i+1] > 0 and A[i+1] - A[i] > 1:
                return A[i] + 1
        return A[-1] + 1