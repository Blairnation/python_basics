class Car:
    def __init__(self, model,make):
       self.model = model
       self.make = make

    def move(self):
        print(f'{self.model} moved')

class Motor(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make)  
        self.year = year

car = Car('buga', 'tti')

motor = Motor('lambo', 'ghini', 2000)
motor.move()             