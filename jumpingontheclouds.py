'''
Problem Statement url
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

'''

''' solution  '''


def jumpingOnClouds(c):
    ans = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 >= len(c) or c[i + 2] == 1:
            i = i + 1
            ans = ans + 1
        else:
            i = i + 2
            ans = ans + 1

    return ans


print(jumpingOnClouds(c=[0, 0, 1, 0, 0, 1, 0]))
