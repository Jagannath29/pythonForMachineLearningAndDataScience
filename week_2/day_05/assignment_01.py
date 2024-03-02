# # Advanced Inheritance and Abstract Classes

# ## Objective

# Create a set of classes representing different animals, introducing multiple levels of inheritance and abstract classes.

# ## Requirements

# 1. Create an abstract class called `Animal` with abstract methods:
#    - `speak`: Abstract method representing the sound the animal makes.
#    - `move`: Abstract method representing how the animal moves.
#    - `eat`: Abstract method representing what the animal eats.

# 2. Implement three concrete classes: `Mammal`, `Bird`, and `Fish`, inheriting from the `Animal` class. Implement the abstract methods accordingly.

# 3. Create concrete classes for specific animals within each category:
#    - For `Mammal`: Implement classes like `Dog` and `Cat`.
#    - For `Bird`: Implement classes like `Eagle` and `Penguin`.
#    - For `Fish`: Implement classes like `Salmon` and `Goldfish`.

# 4. Add unique methods for each specific animal:
#    - For example, `bark` for `Dog`, `fly` for `Eagle`, `swim` for `Salmon`.

# 5. Demonstrate the usage of these classes by creating instances and calling various methods.    


from abc import ABC, abstractmethod
class Animal:
    
    def __init__(self, name, sound, speed, food):
        self.name = name
        self.sound = sound
        self.speed = speed
        self.food = food
    
        @abstractmethod
        def speak(self):
            pass

        @abstractmethod
        def move(self):
            pass

        @abstractmethod
        def eat(self):
            pass
        
        
class Dog(Animal):
    def __init__(self, name, sound, speed, food):
        super().__init__(name, sound, speed, food)
        
    def speak(self):
        print(f'{self.name} is {self.sound}. ')
    
    def move(self):
        print(f'{self.name} is {self.speed}. ')
        
    def eat(self):
        print(f'{self.name} is {self.food}. ')
        
        
dog = Dog('Dog', 'barking','moving fast', 'eating' )
dog.speak()
dog.move()
dog.eat()

print('\n')

class Fish(Animal):
    def __init__(self, name, sound, speed, food):
        super().__init__(name, sound, speed, food)
        
    def speak(self):
        print(f'{self.name} is {self.sound}. ')
    
    def move(self):
        print(f'{self.name} is {self.speed}. ')
        
    def eat(self):
        print(f'{self.name} is {self.food}. ')
        
        
fish = Fish('Jelly fish', 'talking','swimming fast', 'eating' )
fish.speak()
fish.move()
fish.eat()


print('\n')

class Bird(Animal):
    def __init__(self, name, sound, speed, food):
        super().__init__(name, sound, speed, food)
        
    def speak(self):
        print(f'{self.name} is {self.sound}. ')
    
    def move(self):
        print(f'{self.name} is {self.speed}. ')
        
    def eat(self):
        print(f'{self.name} is {self.food}. ')
        
        
bird = Bird('Bird', 'talking','flying high', 'eating' )
bird.speak()
bird.move()
bird.eat()


    
        
    
        
    