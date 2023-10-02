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