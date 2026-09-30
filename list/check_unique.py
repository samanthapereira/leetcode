def check_unique(lst):
    # Your code goes here
    checked = []
    for num in lst:
        if num not in checked:
            checked.append (num)
        else: 
            return False
    return True

lst = [1, 2, 3, 4, 5, 3]
print (check_unique(lst))