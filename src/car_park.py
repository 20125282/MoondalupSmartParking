class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.sensors = sensors or []
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
    def __str__(self):
        return "Car park at " + str(self.location) + ", with " + str(self.capacity) + " bays."