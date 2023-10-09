def solution(A, B):
    downstream_fish = []
    alive_fish = 0
    
    for i in range(len(A)):
        if B[i] == 0:
            while downstream_fish and downstream_fish[-1] < A[i]:
                downstream_fish.pop()
            if not downstream_fish:
                alive_fish += 1
        else:
            downstream_fish.append(A[i])
    
    return alive_fish + len(downstream_fish)
