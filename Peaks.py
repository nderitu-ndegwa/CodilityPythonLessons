def solution(A):
    peaks = [i for i in range(1, len(A) - 1) if A[i - 1] < A[i] and A[i] > A[i + 1]]
    if not peaks:
        return 0

    for num_blocks in range(len(peaks), 0, -1):
        if len(A) % num_blocks == 0:
            block_size = len(A) // num_blocks
            current_block = 0

            for peak in peaks:
                if peak // block_size == current_block:
                    current_block += 1

            if current_block == num_blocks:
                return num_blocks

    return 0
