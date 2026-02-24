from abc import ABC, abstractmethod

class Vehicle(ABC):
    vehicle_count = 0

    def __init__(self, brand, model, speed):
        self._brand = brand
        self._model = model
        self.__speed = speed
        Vehicle.vehicle_count += 1

    def set_speed(self, new_speed):
        if new_speed > 0:
            self.__speed = new_speed

    def get_speed(self):
        return self.__speed
    
    @abstractmethod
    def drive(self):
        pass

    def show_details(self):
        print(f"{self._brand}, {self._model}, Speed: {self.get_speed()} km/h")


class Car(Vehicle):

    def __init__(self, brand, model, speed, fuel_type):
        self._fuel_type = fuel_type
        super().__init__(brand, model, speed)  # mathi pathako

    def drive(self):
        print(f"CAR is moving now")

    def show_details(self):
        print(
            f" CAR {self._brand} {self._model}, Speed: {self.get_speed()} km/h,\
fuel type: {self._fuel_type}"
        )


class Bike(Vehicle):
    def __init__(self, brand, model, speed, has_gear):
        self._has_gear = has_gear
        super().__init__(brand, model, speed)

    def drive(self):
        print(f"BIKE {self._brand} is zooming through trafic")

    def show_details(self):
        print(
            f" BIKE {self._brand} {self._model}, Speed: {self.get_speed()} km/h,\
Gear: {self._has_gear}"
        )


class Bus(Vehicle):
    def __init__(self, brand, model, speed, capacity):
        self._capacity = capacity
        super().__init__(brand, model, speed)

    def drive(self):
        print(f"BUS {self._brand} is carrying passengers")

    def show_details(self):
        print(
            f" BUS {self._brand} {self._model}, Speed: {self.get_speed()} km/h,\
capacity: {self._capacity}"
        )


"""
c1 = Car("totata", 2002, 45, "Petrol")
c1.drive()
c1.show_details()

b1 = Bike("yamaha", 2017, 40, True)
b1.drive()
b1.show_details()

bus1 = Bus("Volvo", 9700, 35, 40)
bus1.drive()
bus1.show_details()
"""

car1 = Car("Tesla", "Model 3", 45, "Electric")
bike1 = Bike("Yamaha", "FZ", 30, True)
bus1 = Bus("Volvo", "9700", 35, 40)
# --- Test Abstract Base Class behavior --
print("\n=== Testing Abstract Base Class ===")
print("Is Vehicle abstract?", hasattr(Vehicle, "__abstractmethods__"))

# --- Test Inheritance and Polymorphism --
print("\n=== Testing Polymorphism (drive methods) ===")
vehicles = [car1, bike1, bus1]
for v in vehicles:
    v.drive()  # each should print different message

# --- Test Encapsulation (private attribute access)
print("\n=== Testing Encapsulation (speed setter/getter) ===")
car1.set_speed(120)
bike1.set_speed(80)
bus1.set_speed(60)
print(car1.get_speed())  # Expected 120
print(bike1.get_speed())  # Expected 80
print(bus1.get_speed())  # Expected 60


# Direct access should fail (if encapsulation is correct)
print("\nTrying to access private attribute directly:")
try:
    print(car1.__speed)
except AttributeError:
    print("Access denied: private attribute is encapsulated properly")

# --- Test show_details method override --
print("\n=== Testing show_details() ===")
for v in vehicles:
    v.show_details()  # each should include its specific attributes

# --- Test class vs instance variable --
print("\n=== Testing class variable (vehicle_count) ===")
print("Vehicle count:", Vehicle.vehicle_count)

# Check that instance doesn’t override class variable accidentally
car1.vehicle_count = 99
print("Vehicle.vehicle_count =", Vehicle.vehicle_count)
print("car1.vehicle_count =", car1.vehicle_count, "(should not affect\
class variable)")

# --- Test inheritance chain --
print("\n=== Testing inheritance relationships ===")
print(isinstance(car1, Vehicle))  # True
print(isinstance(bike1, Vehicle))  # True
print(isinstance(bus1, Vehicle))  # True
print(issubclass(Car, Vehicle))  # True
print(issubclass(Bike, Vehicle))  # True
print(issubclass(Bus, Vehicle))  # True
print("\nAll tests executed.")

print(f"Final vehicle count {Vehicle.vehicle_count} ")
