def solution(S):
    if len(S) % 2 != 0:
        return 0
    
    stack = []
    for char in S:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return 0
            if stack[-1] != '(':
                return 0
            stack.pop()
    
    if not stack:
        return 1
    else:
        return 0
