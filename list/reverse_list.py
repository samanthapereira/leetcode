def reverse_list(lst):
    # Your code goes here
    reversed = []
    for i in range(len(lst)-1, -1, -1):
        reversed.append(lst[i])
    return reversed

lst = [10,90,30,10,40]
print (reverse_list(lst))