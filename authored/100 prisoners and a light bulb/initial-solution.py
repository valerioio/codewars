class Prisoner:
    def __init__(self, name, counter):
        self.name = name
        self.counter = counter
    def enter_room(self, light_bulb):
        return self.toggle(light_bulb), self.make_assertion()
    def toggle(self, light_bulb):
        return not light_bulb
    def make_assertion(self):
        return False

def gather_and_discuss():
    return tuple(Prisoner('John Doe', i) for i in range(100))
