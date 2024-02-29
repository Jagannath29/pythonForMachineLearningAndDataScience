# **`Q.8 Write a python function to print the even numbers from a given list.`**
def even(num):
    even_num = [i for i in num if i%2 == 0]
    print(f'The even number in the list are: {even_num}')

even(num=[1, 2, 3, 4, 5, 6, 7, 8, 9])