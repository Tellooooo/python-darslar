class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(self.model + " " + self.color)


cobalt = Car('Cobalt', 'White')
nexia = Car('Nexia', 'Black')

cobalt.info()
nexia.info()