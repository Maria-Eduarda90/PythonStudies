class Vehicle():
    def __init__(self, color, wheel, mark, tank):
        self.color = color
        self.wheel = wheel
        self.mark = mark
        self.tank = tank

    def to_fuel(self, liters):
        self.tank += liters