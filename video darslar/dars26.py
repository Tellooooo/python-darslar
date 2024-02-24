class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_model(self):
        return self.model.upper()
    
    def get_color(self):
        return self.color.upper()
    
    def set_color(self, color):
        self.color = color

    def info(self):
        print(self.model + " " + self.color)


cobalt = Car('Cobalt', 'White')
nexia = Car('Nexia', 'Black')

cobalt.set_color('red')

# cobalt.info()
# nexia.info()

# print(cobalt.get_model())
# print(cobalt.color)

print(cobalt.get_color())