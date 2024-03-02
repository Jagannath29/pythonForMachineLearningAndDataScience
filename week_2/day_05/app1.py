# class Animal:
#     def __init__(self, name, color, height):
#         self.name = name
#         self.color = color
#         self.height = height
        
        
#     def _init__(self, name, color):
#         self.name = name
#         self.color = color
        
    
#     def display(self):
#         print(f'The {self.height} height is tall ')
        
        
# if __name__ == '__main__':
#     animal = Animal('dog')
    
#     animal.display()
    
class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        if len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.species = args[2]

    
        
    
    def display(self):
        print(f'The {self.name} height is tall ')
        
        
if __name__ == '__main__':
    animal = Animal('dog', )
    
    animal.display()