# **`Q.6 Write a python function that takes a list and returns a new list with unique elements of the first list`**

def unique(number):
    uniq = []
    for num in number:
        if num not in uniq:
            uniq.append(num)
            
    print(f'Numbers in a new list are: {uniq}')

num = [ 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
unique(num)