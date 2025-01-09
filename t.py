class Taksopark:
    def __init__(self,title):
        self.title=title
        self.balance=0
        self.cars = []
        self.safarlar = []

    def add_car(self,car):
        self.cars.append(car)