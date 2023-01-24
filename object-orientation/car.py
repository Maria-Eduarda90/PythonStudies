from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, color, mark, tank):
        Vehicle.__init__(self, color, 4, mark, tank)

    def to_fuel(self, liters):
        if self.tank + liters > 50:
            print("Error: tanque cheio")
        else:
            self.tank += liters