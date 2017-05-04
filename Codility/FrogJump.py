import math
def solution(X, Y, D):
    # write your code in Python 2.7
    r = Y - X
    r = r / float(D)	# float makes it possible for ceil to get the right result. without it some test cases will  fail
    return(int(math.ceil(r)))