from vehicle import Vehicle
from car import Car

car = Vehicle('red', 4, 'ford', 10)

print("Cor: ", car.color)
print("Wheel: ", car.wheel)
print("Mark: ", car.mark)
print("Tank: ", car.tank)
car.to_fuel(20);
print("")
print("Tank: ", car.tank)
print("")
print("*****************************************")

car_blue = Car('blue', 'bmw', 30)
print("Cor: ", car_blue.color)
print("Mark: ", car_blue.mark)
print("Tank: ", car_blue.tank)
car_blue.to_fuel(10);
print("")
print("Tank: ", car_blue.tank)