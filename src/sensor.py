import random
class Sensor:
    def __init__(self, id, is_active=False):
        self.id = id
        self.is_active = is_active

    def update_car_park(self, car_park, plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self, car_park):
        plate = self._scan_plate()
        self.update_car_park(car_park, plate)

    def __str__(self):
        return "Sensor" + str(self.id) + ":" + str(self.is_active) + "."

class EntrySensor(Sensor):
    def update_car_park(self, car_park, plate):
        car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, car_park, plate):
        car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

        def _scan_plate(self, car_park):
            return random.choice(car_park.plates)
