class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} is starting."

    def stop(self):
        return f"{self.make} {self.model} is stopping."
    
    def is_old(self, current_year):
        age = current_year - self.year
        if age > 4:
            return f"The car is a {self.year} model, so it's considered an old car."
        else:
            return f"The car is a {self.year} model, so it's not considered an old car."

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Print the car's status
print(my_car.start())
print(my_car.stop())

# Check if the car is old (assuming the current year is 2024)
print(my_car.is_old(2033))
