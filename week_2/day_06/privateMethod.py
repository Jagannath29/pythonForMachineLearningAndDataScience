'''Private Access --> usess __ for private'''
class Person:
    def __init__(self, name, age): #  name, age are attributes
        self.__name = name
        self.__age = age
        
        
    def display(self):
        print(f'The person name is{self.__name} is {self.__age} years')
        


if __name__ == "__main__":
    person_test = Person(name='Ram', age= 55)
    
    print(person_test._Person__name)       