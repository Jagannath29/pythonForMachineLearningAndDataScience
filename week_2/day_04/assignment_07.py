# **`Q.7 Write a Python function that takes a number as a parameter and check the
# number is prime or not.`**

def primeNum(num):
    if num == 1:
        return False
    elif num == 0:
        return False
    elif num < 1:
        return False
    
    else:
        
        try:
        
            for i in range(3, num - 1):
                if num % i == 0:
                    return False
            else:
                print('Prime number')
                    
        except (ValueError, TypeError) as e:
            print(f'{e} is an invalid input, please enter a valid one')

        
n = 5
primeNum(n)
                