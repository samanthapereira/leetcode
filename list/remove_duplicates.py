def remove_duplicates(lst):
    # Your code goes here
    result_unique = []
    for i in lst: 
        if i not in result_unique:
            result_unique.append(i)
    return result_unique

lst = [1, 2, 2, 3, 4, 4, 5]
print (remove_duplicates(lst))