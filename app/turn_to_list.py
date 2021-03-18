"""
Qns. 4
"""
# Write a program which accepts a sequence of comma-separated numbers
#  from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def turn_into_list(sequence):
    # print(sequence)
    object=  sequence.split(",")
    tuple1 = tuple(object)
    return (object)
    # print(tuple1)
# sequence = input("Please input any number:")
# turn_into_list(sequence)
