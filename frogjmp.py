import math

def solution (X, Y, D):
    diff = Y - X
    jumps  = math.ceil(diff / D)
    
    if (jumps * D) >= diff:
        return jumps