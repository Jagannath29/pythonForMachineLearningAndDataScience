# # Task 01: Word Pyramid Generator

# ## Task

# Create a program that generates a word pyramid pattern based on user input.

# ## Objective 

# The objective is to generate and print a pyramid pattern using the letters of the word provided by the user. Each level of the pyramid should display the letters of the word up to that level, and the word should be centered on each level of the pyramid.

# ## Requirements

# 1. Ask the user to input a word.
# 2. Generate and print a pyramid pattern using the letters of the word.
# 3. Each level of the pyramid should display the letters of the word up to that level.
# 4. The word should be centered on each level of the pyramid.

# ## Additional Challenges

# 1. Implement a function to validate the input and ensure it's a valid word.
# 2. Allow the user to choose the direction of the pyramid (upwards or downwards).
# 3. Enhance the program to handle phrases or sentences instead of single words.

# Expected Output:
# if word level is up:
# ```
#             S    
#            S u   
#           S u n  
#          S u n i 
#         S u n i l
# ```

# if word level is Down:
# ```
#             S u n i l
#              S u n i 
#               S u n  
#                S u   
#                 S 
# ```

def pyramid_up(name):
    length_of_user = len(name)
    
    for row in range(length_of_user):
       
        for column in range(length_of_user-row-1):  # haldles the spaces i.e (length = 5)- (row = 0) - (1) we have 4 space in first row.
            print(" ", end='')
        for row in range(row+1):
            print(name[row], end=' ')
        print()    


def pyramid_down(name):
    length_of_user = len(name)
    for row in range(length_of_user):
        for column in range(row):  
            print(" ", end='')
        
        for column in range(2*(length_of_user-row)-1):
            print(name[row], end='')
        print()

name = input('Enter Your name: ')
up_down = input('Enter up or down: ')
lst = ['up', 'down']
if up_down == 'up':
    pyramid_up(name)
elif up_down == 'down':
    pyramid_down(name)
    
else:
    print('Invalid input')
    
    







    

    