
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


school_bus = Bus("School volvo", 12, 41)
print(school_bus.name, school_bus.mileage, school_bus.capacity)
print(type(school_bus))
