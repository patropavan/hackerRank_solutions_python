'''
Problem Statement url
https://www.hackerrank.com/challenges/apple-and-orange/problem
'''

''' solution  '''


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # house_coordinate_stretch = s and (t+1)
    # apple_tree_coordinate = a
    # orange_tree_coordinate = b

    no_of_apples_on_sam_house = 0
    no_of_oranges_on_same_house = 0

    actual_distances_covered_apples = [a + x for x in apples]
    actual_distances_covered_orange = [b + y for y in oranges]

    for apple_distance in actual_distances_covered_apples:
        if apple_distance in range(s, t + 1):
            no_of_apples_on_sam_house = no_of_apples_on_sam_house + 1

    for orange_distance in actual_distances_covered_orange:
        if orange_distance in range(s, t + 1):
            no_of_oranges_on_same_house = no_of_oranges_on_same_house + 1

    print(no_of_apples_on_sam_house, no_of_oranges_on_same_house, sep='\n')


countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3,-2,-4])
