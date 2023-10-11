import math

def solution(N):
    min_perimeter = float('inf')
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            perimeter = 2 * (i + N//i)
            if perimeter < min_perimeter:
                min_perimeter = perimeter
    return min_perimeter
