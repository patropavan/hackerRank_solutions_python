'''
Problem Statement url
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


'''

''' solution  '''

def rotLeft(a, d):
    i = d%len(a)
    return(a[i:]+a[:i])