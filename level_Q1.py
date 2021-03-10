#!/usr/bin/python
import math
"""
Qns. 6
"""
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

def square_root(sequence):
    answer_list=[]
    C=50
    H=30
    D= sequence
    list1=D.split(",")
    
    for item in list1:
        # print(float(item))
        ans=2 * C * float(item)/ H
        # print(ans)
        sqrt_ans=math.sqrt(ans)
        answer_list.append(str(math.floor(sqrt_ans)))
    return (",".join(answer_list)) #join method applies to strings only
sequence = input("Please input any number in comma separated input sequence:")
print(square_root(sequence))

# Write a program that accepts a comma separated sequence of words as input
#  and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sort_string(sequence):
    list1 = sequence.split(",")
    list1.sort()
    return (",".join(list1)) #join method applies to strings only
sequence = input("Please input words in a comma-separated sequence:")
print(sort_string(sequence))

# Write a program that accepts sequence of lines as input and prints
#  the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
def sort_string(sequence):
    print(sequence.upper())
sequence = input("Please input sentence:")
print(sort_string(sequence))

