import math
def solution(A):
    # write your code in Python 2.7
    b = set(sorted(A))
    c = set(range(1,len(A)+1))
    
    x = c-b
    if x:
        return min(x)
    else:
        return len(A)+1