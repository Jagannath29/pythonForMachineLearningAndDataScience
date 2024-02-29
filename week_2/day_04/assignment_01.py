# **`Q.1 Write a python function to multiply all the numbers in a list`**

def multiplyList(myList):
    product = 1
    for num in myList:
        product *= num
    return product
    
    
lst = [1, 2, 3, 4]
print(multiplyList(lst))