class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, name, model, year, doors):
        super().__init__(name, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")
        print("Vehicle Type: Car")


class Motorcycle(Vehicle):
    def __init__(self, name, model, year, engine_size):
        super().__init__(name, model, year)
        self.engine_size = engine_size

    def display_info(self):
        super().display_info()
        print(f"Engine Size: {self.engine_size}")
        print("Vehicle Type: Motorcycle")

my_car = Car("Toyota", "Random", 2000, 4)
my_motorcycle = Motorcycle("Yamaha", "FZR", 2023, "600cc")

# Display
print("Car Details:")
my_car.display_info()
print("\nMotorcycle Details:")
my_motorcycle.display_info()
