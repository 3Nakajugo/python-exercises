#!/usr/bin/python
"""
Qns. 1
"""
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
number_list = []
for number in range(2000, 3200):
    if number%7==0 and number%5==1:
        # number_list.append(number)
        number_list.append(str(number))
# print(number_list)
print(','.join(number_list))

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

number = int(input("Please input any number:"))
print(number_factorial(number))

"""
Qns. 3
"""
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def generate_dict(number):
    dict = {}
    count = 1
    while (count <= number):
        dict[count] = count * count
        count = count+1
    return dict  
        
number = int(input("Please input any number:"))
print(generate_dict(number))

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
    print(sequence)
    object=  sequence.split(",")
    tuple1 = tuple(object)
    print(object)
    print(tuple1)
sequence = input("Please input any number:")
turn_into_list(sequence)

"""
Qns. 5
"""
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class GetString():

    # def __init__(self, string_input):
        # self.string_input = string_input
    def __init__(self):
        self.string_input = ""

    def get_string(self):
        self.string_input = input("Please input sting ")
    
    def print_string(self):
        print(self.string_input.upper())
# string = GetString("")
string = GetString()
string.get_string()
string.print_string()










