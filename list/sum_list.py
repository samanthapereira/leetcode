def sum_list(numbers):
    # Your code goes here
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum
    pass

numbers = [10, -5, 7, 8, -2]
print (sum_list(numbers))