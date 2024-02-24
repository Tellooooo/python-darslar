class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

# MODELNI CHAQIRISH
    def get_model(self):
        return self.model.upper()
    
# COLORNI CHAQIRISH
    def get_color(self):
        return self.color.upper()
    
# COLORNI ALISHTIRIH
    def set_color(self, color):
        self.color = color
    
    @property
    def info(self):
        return self.model + " " + self.color
    
    @info.setter
    def info(self, name):
        self.model, self.color = name.split(' ')

    @info.deleter
    def info(self):
        self.model = " "
        self.color = " "


cobalt = Car('Cobalt', 'White')
nexia = Car('Nexia', 'Black')

del cobalt.info

# cobalt.info = "Nexia Black"

# COLORNI ALIHTIRISH
# cobalt.set_color('red')

# cobalt.info()
# nexia.info()

# COLORNI CHAQIRISH
# print(cobalt.get_model())
# print(cobalt.color)

# COLORNI CHAQIRISH
# print(cobalt.get_color())

print(cobalt.info)