def binary_search(input_array, value):
    """Your code goes here."""
    input_array.sort
    low_index = int(0)
    high_index = int(len(input_array)-1)
    while(low_index <= high_index):
      middle_index = int((low_index + high_index)/2)
      if (input_array[middle_index]==value):
        return middle_index
      elif (input_array[middle_index]<value):
        low_index = middle_index + 1
      else:
        high_index = middle_index - 1    
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))