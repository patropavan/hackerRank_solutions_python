'''
Problem Statement url
https://www.hackerrank.com/challenges/counting-valleys/problem

'''

''' solution  '''


def countingValleys(steps, path):
    height = 0
    prev_height = 0
    cnt = 0
    for i in range(len(path)):
        if (path[i] == 'U'):
            height += 1
        elif path[i] == 'D':
            height -= 1
        if height == 0 and prev_height < 0:
            cnt += 1
        prev_height = height

    return cnt


print(countingValleys(12, "DDUUDDUDUUUD"))