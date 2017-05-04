def solution(A):
    # write your code in Python 2.7
    b = [0] * (len(A)+2)
    
    for i in range(0,len(A)):
        b[A[i]] = 1
    #print b
    for i in range(1,len(b)):
        if b[i] == 0:
            return i
        
    return 0