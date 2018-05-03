import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from driver import Driver

class TestClassMethodsClassVariables(unittest.TestCase):

    def test_driver_class_init(self):
        driver_1 = Driver("Terrance", "Toyota", "Camry")
        driver_2 = Driver("Rachel", "Subaru", "Forrester")
        driver_3 = Driver("Jeff", "Toyota", "Camry")
        driver_4 = Driver("Lore", "Honda", "Pilot")
        self.assertItemsEqual(Driver._all, [driver_1, driver_2, driver_3, driver_4])
        self.assertEqual(Driver._count, 4)

    def test_fleet_size_class_method(self):
        self.assertEqual(Driver.fleet_size(), 4)

    def test_driver_names_class_method(self):
        self.assertItemsEqual(Driver.driver_names(), ["Terrance", "Rachel", "Jeff", "Lore"])

    def test_fleet_makes_class_method(self):
        self.assertItemsEqual(Driver.fleet_makes(), ["Toyota", "Toyota", "Subaru", "Honda"])

    def test_fleet_models_class_method(self):
        self.assertItemsEqual(Driver.fleet_models(), ["Camry", "Camry", "Forrester", "Pilot"])

    def test_fleet_makes_count_class_method(self):
        self.assertEqual(Driver.fleet_makes_count(), {'Honda': 1, 'Toyota': 2, 'Subaru': 1})

    def test_fleet_models_count_class_method(self):
        self.assertEqual(Driver.fleet_models_count(), {'Pilot': 1, 'Camry': 2, 'Forrester': 1})

    def test_percent_of_fleet_class_method(self):
        self.assertEqual(Driver.percent_of_fleet("Toyota"), "50.0%")
