def my_function(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(5, 5)
print(result)  # Output: 5

#Alternative solution using max function which already handles the edge case
def my_function_alternative(a,b):
  return max(a,b)