class Animal:
    def sound(self):
        print('sound')


class Dog:
    def sound(self):
        print(' barks')
        
        
def talk(sounds):
    sounds.sound()
        
if __name__ == '__main__':
    
    animal = Animal()
    dog = Dog()
    talk(animal)
    talk(dog)
    
        
    