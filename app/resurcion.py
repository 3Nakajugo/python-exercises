"""
A recursive function should call itself.
it should have a base case. NB:Base cases can be more than one.
"""
def get_fib(position):
  if position ==0:
    return 0
  elif position ==1:
    return 1
  else :
    return get_fib(position - 1) + get_fib(position - 2) 
  
print(get_fib(10))