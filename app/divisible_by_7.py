#!/usr/bin/python
"""
Qns. 1
"""
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def divisible_by_7():
    number_list = []
    for number in range(2000, 3200):
        if number%7==0 and number%5==1:
            # number_list.append(number)
            number_list.append(str(number))
    # print(number_list)
    return (','.join(number_list))
