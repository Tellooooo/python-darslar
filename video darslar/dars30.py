class Car:
    color = 'green'

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
        return self.model + " " + self.c()
    
    @info.setter
    def info(self, name):
        self.model, self.color = name.split(' ')

# INFO QISMINI BO'SHATISH
    @info.deleter
    def info(self):
        self.model = " "
        self.color = " "

    @classmethod
    def c(self):
        return self.color
    
    @staticmethod
    def s(x):
        return x*x


print(Car.s(2))


# cobalt = Car('Cobalt', 'White')
# nexia = Car('Nexia', 'Black')


# print( getattr(cobalt, 'info'))