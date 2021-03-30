'''
Problem Statement url
https://www.hackerrank.com/challenges/repeated-string/problem

'''

''' solution  '''



# Complete the repeatedString function below.
def repeatedString(s, n):
    string_length = len(s)
    repetition_num = n
    # if the length of the string is 0
    if string_length == 0:
        return 0

    # if the length is 1 and doesn't contain the character 'a'
    elif string_length == 1 and 'a' not in s:
        return 0

    # if length of the string is 1 and contains the character 'a'
    elif string_length == 1 and 'a' in s:
        return n
    # if length of the string is greater than 1
    elif string_length > 1:
        # string repetition compuataion
        if n % string_length == 0:
            # total number of repetition is
            repeated_string = s * (repetition_num // len(string_length))
            # count the number of 'a's in the repeated string:
            count = repeated_string.count('a')
        else:
            # total number of repetition is
            repeated_string = s * (repetition_num // string_length) + s[0:(repetition_num % string_length)]
            # count the number of 'a's in the repeated string:
            count = repeated_string.count('a')

        return count

    return 0