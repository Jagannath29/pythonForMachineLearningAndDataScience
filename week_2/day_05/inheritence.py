class Car:
    def __init__(self, name, door, fuel):
        self.name = name
        self.door = door
        self.fuel = fuel
        
        
class Maruti(Car):
    def __init__(self, name, door, fuel, speed):
        super().__init__(name, door, fuel)
        self.speed = speed
        
    def tarvel(self):
        print(f'{self.name}: {self.speed}')
            

if __name__ == '__main__':
    suz = Maruti('Suzaki',4, 'electric' , 80 )
    suz.tarvel()

