def solution(H):
    stack = []
    blocks = 0
    for height in H:
        while stack and stack[-1] > height:
            stack.pop()
        if not stack or stack[-1] < height:
            blocks += 1
            stack.append(height)
    return blocks
