import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, self.car_park, True)
        self.exit_sensor = ExitSensor(2, self.car_park, True)
        # self.sensor = Sensor(1, self.car_park, True)

    def test_entry_sensor_initialized_with_all_attribute(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_exit_sensor_initialized_with_all_attribute(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_entry_sensor_detect_vehicle(self):
        initial_bays = self.car_park.available_bays
        self.entry_sensor.detect_vehicle()
        updated_bays = self.car_park.available_bays
        self.assertNotEqual(initial_bays, updated_bays)

    def test_exit_sensor_detect_vehicle(self):
        self.car_park.add_car("FAKE-001")
        initial_bays = self.car_park.available_bays
        self.exit_sensor.detect_vehicle()
        updated_bays = self.car_park.available_bays
        self.assertNotEqual(initial_bays, updated_bays)


if __name__ == "__main__":
    unittest.main()