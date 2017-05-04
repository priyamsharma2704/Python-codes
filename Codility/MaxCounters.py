def solution(N, A):
    # write your code in Python 2.7
    
    r = [0] * N
    
    for i in A:
        if i <= N:
            r[i-1] = r[i-1]+1
        else:
            r = [max(r)] * N
    return r