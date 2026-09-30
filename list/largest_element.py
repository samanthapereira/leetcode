def find_largest(numbers):
    # Your code goes here
    max = numbers[0]
    for i in numbers:
        if i > max: 
            max = i
    return max
    pass


numbers = [5, 2, 9, 3, 7]
print(find_largest(numbers))
    
