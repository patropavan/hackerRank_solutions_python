'''
Problem Statement url
https://www.hackerrank.com/challenges/2d-array/problem


'''

''' solution  '''


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hg_sum = -63  # as the minimum value of each element in an hour glass is -9, hence -9*7 =63
    len_arr = len(arr)

    for row in range(1, len_arr - 1):
        for col in range(1, len_arr - 1):
            hg_current_sum = arr[row][col] + arr[row - 1][col - 1] + arr[row - 1][col] + arr[row - 1][col + 1] + \
                             arr[row + 1][col - 1] + arr[row + 1][col] + arr[row + 1][col + 1]

            if hg_current_sum > hg_sum:
                hg_sum = hg_current_sum

    return hg_sum