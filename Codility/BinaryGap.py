# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    n = N
    bit = bin(n)
    b = []
    l = []
    c = 0
    m = 0
    
    for i in bit:
        b.append(i)
    #print b  
    b.remove(b[0])
    #print b 
    b.remove(b[0])
    #print b
    for i in b:
        if i == '0':
            c += 1
        else:
            l.append(c)
            c = 0
    #print l
    for i in l:
        if i > m:
            m = i
        
    return m