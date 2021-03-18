# Question 7
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
#  The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

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
sequence = input("Please input any number:")
print(square_root(sequence))
