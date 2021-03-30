'''
Problem Statement url
https://www.hackerrank.com/challenges/sock-merchant/problem


'''

''' solution  '''

def sockMerchant(n, ar):
    sorted_socks_set = list(set(sorted(ar)))
    pair = 0
    sock = 0
    while sock < len(sorted_socks_set):
        count = ar.count(sorted_socks_set[sock])
        if count % 2 == 0:
            pair += count // 2
        elif count % 2 != 0 and count > 1:
            pair += count // 2
        sock = sock + 1

    return pair


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]
                   ))
