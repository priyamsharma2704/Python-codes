def solution(A):
    # write your code in Python 2.7
    if len(set(A)) == len(A) and max(A) == len(A): # set(A) puts the list elements in an order
        return 1
    else:
        return 0