import unittest
from Tires.carrigan_tire import carrigan

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_list = [0.5, 0.8, 0.2, 1]
        tire = carrigan(sensor_list)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_list = [0.5, 0.8, 0.2, 0.4]
        tire = carrigan(sensor_list)
        self.assertFalse(tire.needs_service())
    

if __name__ == '__main__':
    unittest.main()
