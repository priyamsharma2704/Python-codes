def solution(A, K):
    # write your code in Python 2.7
    r = [0] * len(A)
    
    for i in range (len(A)):
        r[(i+K) % len(A)] = A[i]
    return r