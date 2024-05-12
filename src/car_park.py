class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []
        self.plates = plates or []
        self.displays = displays or []

    def register(self, component):
        from sensor import Sensor  # Import moved here
        from display import Display  # Import moved here
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        else:
            raise TypeError("Object must be a Sensor or Display")

    def add_car(self, plate):
        from display import Display  # Import moved here
        if len(self.plates) < self.capacity:
            self.plates.append(plate)
            self.update_displays()
        else:
            print("Car park is full.")

    def remove_car(self, plate):
        from display import Display  # Import moved here
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
        else:
            raise ValueError(f"Plate {plate} is not in the carpark.")

    @property
    def available_bays(self):
        if len(self.plates) >= self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_displays(self):
        from display import Display  # Import moved here
        data = {
            "available_bays": self.available_bays,
            "temperature": 25
        }

    def __str__(self):
        return "Car park at " + str(self.location) + ", with " + str(self.capacity) + " bays."
