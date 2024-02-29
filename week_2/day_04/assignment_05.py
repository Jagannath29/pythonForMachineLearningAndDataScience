# **`Q.5 Write a python function that accepts a string and calculate the number of upper case letters and lower case letters`**
def calculateUpperLowerLetters(myString):
    upper = 0
    lower = 0
    try:
        for letter in myString:
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
        print(f'The number of upper letter are {upper}')
        print(f'The number of lower letter are {lower}')
        
    except (ValueError, TypeError) as e:
        print('There is something error in your message')
    
 
        
stri = 'hello hoW ARE You'
calculateUpperLowerLetters(stri)
             