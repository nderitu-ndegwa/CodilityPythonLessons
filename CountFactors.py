import math

def solution(N):
    count = 0
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            count += 2
    if int(math.sqrt(N))**2 == N:
        count -= 1
    return count
