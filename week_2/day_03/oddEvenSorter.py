# # Task 02: List Manipulation - Odd-Even Sorter

# ## Objective

# Create a program that takes a list of numbers from the user, sorts them into two separate lists (one for odd numbers and one for even numbers), and displays the sorted lists.

# ## Requirements

# 1. Ask the user to input a list of numbers (comma-separated).
# 2. Sort the numbers into two lists: one for odd numbers and one for even numbers.
# 3. Display both lists.

# ## Additional Challenges

# 1. Allow the user to input any type of values (not just numbers) and handle different data types.
# 2. Enhance the program to display the sorted lists in ascending or descending order.

def oddEvenSorter(number_list):
    even_list = [even for even in number_list if (even % 2 == 0)]
    odd_list = [odd for odd in number_list if (odd % 2 != 0)]
    
    # for index in number_list:
    #     if index % 2 == 0:
    #         even_list.append(index)
    #     elif index % 2 != 0:
    #         odd_list.append(index)
    #     else:
    #         print('invalid input')
    
    
    return odd_list, even_list

my_list = [1, 2, 3, 4, 5, 6]
# my_list = list(map(int, input())) did not work
# for i in range(my_list):
#     inp = int(input("Enter a list of a number: "))
#     my_list.append(inp)
print(oddEvenSorter(my_list))
  