class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Bus(Car):
    def __init__(self, model, color, seats):
        self.seats = seats
        super().__init__(model, color)


    def info(self):
        return self.model + " " + self.color + " " + str(self.seats)

b = Bus('Man', 'White', 22)

print(b.info())