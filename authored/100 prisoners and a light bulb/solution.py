class Prisoner:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
    def enter_room(self, light_bulb, current_day):
        if self.name == 'beta' and not light_bulb and self.serial_number:
            self.serial_number -= 1
            light_bulb = True
        elif self.name == 'alpha' and light_bulb:
            self.serial_number -= 1
            return False, not self.serial_number
        return light_bulb, False

def gather_and_discuss():
    return tuple(Prisoner('beta', 1) if i else Prisoner('alpha', 99) for i in range(100))
