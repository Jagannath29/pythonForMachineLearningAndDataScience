# # Advanced Inheritance with Multiple Levels

# ## Objective

# Create a set of classes representing different types of vehicles, introducing multiple levels of inheritance, and demonstrating the use of `super().__init__`.

# ## Requirements

# 1. Create a base class called `Vehicle` with the following attributes:
#    - `make`: Make of the vehicle (e.g., Ford, Honda).
#    - `model`: Model of the vehicle (e.g., Civic, F-150).
#    - `year`: Year of manufacture.
#    - `fuel_type`: Type of fuel the vehicle uses (e.g., Gasoline, Electric).

# 2. Create two subclasses: `Car` and `Truck`, inheriting from the `Vehicle` class. Implement the `__init__` method using `super().__init__` to initialize attributes from the parent class.

# 3. Create a subclass of `Car` called `ElectricCar`. Add an additional attribute:
#    - `battery_capacity`: Capacity of the electric car's battery in kWh.

# 4. Create a subclass of `Truck` called `HybridTruck`. Add an additional attribute:
#    - `electric_motor_power`: Power of the electric motor in the hybrid truck.

# 5. Demonstrate the usage of these classes by creating instances and displaying information about the vehicles.


class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        
    def make(self):
        print(f'Make: {self.make}')
        
    def model(self):
        print(f'Model: {self.model}')
        
    def year(self):
        print(f'Year: {self.year}')
    
    def fuel_type(self):
        print(f'Fuel type: {self.fuel_type}')
        



class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)
        
class ElectricCar(Car):
    def __init__(self, make, model, year, fuel_type, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(make, model, year, fuel_type)
        
    
    def battery(self):
        print(f'Battery is {self.battery_capacity}')
        
# ecar = ElectricCar('BMW', 'f-1', '1994 march', 'Electric', '10 kwh')
# ecar.make()
# ecar.model()
# ecar.year()
# ecar.fuel_type()
# ecar.battery()     


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)
        
class HybridTruck(Truck):
    def __init__(self, make, model, year, fuel_type, electric_motor_power):
        self.electric_motor_power = electric_motor_power
        super().__init__(make, model, year, fuel_type)
        
    
    def electric_motor_power(self):
        print(f'electric motor power is {self.electric_motor_power}') 
        
if __name__ == '__main__':        
    truck = Truck('Dozer', 'JCB', '1999 may', 'fuel')
    truck.model()

