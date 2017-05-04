
def solution(A):
    # write your code in Python 2.7
    a = A[0]
    for i in range(1,len(A)):
        b = A[i]
        a = a ^ b
    return a