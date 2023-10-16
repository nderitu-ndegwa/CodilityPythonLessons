'''


A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..200,000];
        string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.

'''

def solution(S):
    stack = []
    for char in S:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return 0
            if char == ')' and stack[-1] != '(':
                return 0
            elif char == '}' and stack[-1] != '{':
                return 0
            elif char == ']' and stack[-1] != '[':
                return 0
            stack.pop()
    if not stack:
        return 1
    else:
        return 0
