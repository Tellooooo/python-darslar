class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print("Bu Car class")


class ElectroCar:
    def info(self):
        print("Bu ElectroCar class")


class Sedan(Car, ElectroCar):
    pass

s = Sedan("Spark", "white")
# class Bus(Car):
#     def __init__(self, model, color, seats):
#         self.seats = seats
#         print(super())
#         super().__init__(model, color)

#     def info(self):
#         return self.model + " " + self.color + " " + str(self.seats)
    
# class ElecticBus(Bus):
#     def __init__(self, model, color, seats, distance):
#         self.distance= distance
#         print(super())
#         super().__init__(model, color, seats,)  

#     def info(self):
#            return self.model + " " + self.color + " " + str(self.seats) + ' ' + str(self.distance) + "km"

    
# b = ElecticBus ('Man', 'white', 25, 200)

# print(b.info())
# class Truck(Car):
#     def __init__(self, model, color, weight):
#         self.weight = weight
#         super().__init__(model, color)

#     def info(self):
#         return self.model + " " + self.color + " " + str(self.weight) + 't'

# t = Truck("Kamaz", 'Black', 15)


# print(t.info())