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
        self.string_input = input("Please input string ")
    
    def print_string(self):
        print(self.string_input.upper())
# string = GetString("")
string = GetString()
string.get_string()
string.print_string()
