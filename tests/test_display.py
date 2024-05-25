import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        # Create a Display object and a CarPark object for each test case
        self.car_park = CarPark(location="Main Street", capacity=50)
        self.display = Display(id=1, message="Welcome to the car park", is_on=True, car_park=self.car_park)

    def test_display_initialized_with_all_attributes(self):
        # Test that the Display object was initialized with the correct attributes
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        # Test that the update method updates the message attribute
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")

if __name__ == "__main__":
    unittest.main()

