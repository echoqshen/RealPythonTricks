from collections import namedtuple
car = namedtuple('Car', 'color mileage')

my_car = car('red', 10812.46)
print(my_car.color)
print(my_car.mileage)
print(my_car)