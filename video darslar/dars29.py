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

# INFO QISMINI BO'SHATISH
    @info.deleter
    def info(self):
        self.model = " "
        self.color = " "


cobalt = Car('Cobalt', 'White')
nexia = Car('Nexia', 'Black')

# del cobalt.info

delattr(cobalt, 'info')

setattr(cobalt, 'info', 'Nexia White')

# CHAQIRILGAN MALUMOT BOY YOKI YOQLIGINI KO'RSATADI
# print( hasattr(cobalt, 'info'))

# CHAQIRILGAN MALUMOTNI CHIQARIB BERADI
print( getattr(cobalt, 'info'))