"""
Qns. 2
"""
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def number_factorial(number):
    # int(number)
    if number == 0:
        return 1
    return number * number_factorial(number - 1)

# number = int(input("Please input any number:"))
# print(number_factorial(number))