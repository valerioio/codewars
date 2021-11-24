light_bulb = False

class Prisoner:
    def __init__(self, name, serial):
        self.name = name
        self.serial = serial
    def enter_room(self):
        global light_bulb
        if self.name == 'beta' and not light_bulb and self.serial:
            self.serial -= 1
            light_bulb = True
        elif self.name == 'alpha' and light_bulb:
            self.serial -= 1
            light_bulb = False
            return not self.serial
        return False

def gather_and_discuss():
    return tuple(Prisoner('beta', 1) if i else Prisoner('alpha', 99) for i in range(100))
