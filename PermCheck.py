def solution(A):
    n = len(A)
    counter = [0] * n

    for num in A:
        if num <= n:
            counter[num - 1] += 1
        else:
            return 0

    for count in counter:
        if count != 1:
            return 0

    return 1