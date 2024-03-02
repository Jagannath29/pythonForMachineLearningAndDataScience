'''
    Class Bank
    method - 

'''

'''
table student

entity -> student
attributes -> std_id, std_name, 

'''
# Class are the collection of objects

class Car:
    def __init__(self, tyres, doors, windows, engine_type):
        self.tyres = tyres
        self.doors = doors
        self.windows = windows
        self.engine_type = engine_type
        self.engine_type = engine_type
        
    def driver(self):
        print(f'The type of the car is {self.engine_type}')
        

if __name__ == '__main__':
    car1 = Car(4, 4, 5, 'hey')
    car2 = Car()
    
    car1.driver()
    # car1.tyres = 4
    # car2.color = 'black'
    # # print(car1, car2)
    # print(dir(car1))