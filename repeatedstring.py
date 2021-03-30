'''
Problem Statement url
https://www.hackerrank.com/challenges/repeated-string/problem

'''

''' solution  '''



# Complete the repeatedString function below.
def repeatedString(s, n):
    x,y = divmod(n,len(s))
    return s[:y].count("a")*(x+1) + s[y:].count("a")*x