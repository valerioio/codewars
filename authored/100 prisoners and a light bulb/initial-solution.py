class Prisoner:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
    def enter_room(self, light_bulb, current_day):
        return self.toggle(), self.make_assertion()
    def toggle(self):
        return not light_bulb
    def make_assertion(self):
        return False

def gather_and_discuss():
    return tuple(Prisoner('John Doe', i) for i in range(100))
