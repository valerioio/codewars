class Prisoner:
    def __init__(self, name, counter):
        self.name = name
        self.counter = counter
    def enter_room(self, light_bulb):
        if self.name == 'beta' and not light_bulb and self.counter:
            self.counter -= 1
            light_bulb = True
        elif self.name == 'alpha' and light_bulb:
            self.counter -= 1
            return False, not self.counter
        return light_bulb, False

def gather_and_discuss():
    return tuple(Prisoner('beta', 1) if i else Prisoner('alpha', 99) for i in range(100))
