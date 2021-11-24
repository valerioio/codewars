light_bulb = False

class Prisoner:
    def __init__(self, name, serial):
        self.name = name
        self.serial = serial
    def enter_room(self):
        self.toggle()
        return self.make_assertion()
    def toggle(self):
        global light_bulb
        light_bulb = not light_bulb
    def make_assertion(self):
        return False

def gather_and_discuss():
    return tuple(Prisoner('John Doe', i) for i in range(100))
