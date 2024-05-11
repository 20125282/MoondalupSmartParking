class Display:
    def __init__(self, id, message="Welcome to the Moondalup carpark", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")

    def __str__(self):
        return "Display" + str(self.id) + ":" + str(self.message) + "."
