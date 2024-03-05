'''Procted Access --> uses single _ '''
class Person:
    def __init__(self, name, age): #  name, age are attributes
        self._name = name
        self._age = age
        
class Ram(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def display(self):
        print(f'The person name is{self._name} is {self._age} years')

    


if __name__ == "__main__":
    person_test = Ram(name='Ram', age= 55)
    # print(person_test._name)
    print(person_test.display())