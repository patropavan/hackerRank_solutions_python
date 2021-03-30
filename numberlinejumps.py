'''
Problem Statement url
https://www.hackerrank.com/challenges/kangaroo/problem

If v1<=v2 , they will never meet.

It is required to check if a solution exists for the following equation:
        x1 + t*v1 == x2 + t*v2

This is equivalent to checking if :
        (x2-x1)%(v1-v2) == 0

'''

''' solution  '''


def kangaroo(x1, v1, x2, v2):
    X = [x1, v1]
    Y = [x2, v2]
    back = min(X, Y)
    print(back)
    fwd = max(X, Y)
    print(fwd)
    dist = fwd[0] - back[0]

    while back[0] < fwd[0]:
        back[0] += back[1]
        fwd[0] += fwd[1]
        if fwd[0] - back[0] >= dist:
            break

    print(["NO", "YES"][back[0] == fwd[0]])


kangaroo(0, 3, 4, 2)
