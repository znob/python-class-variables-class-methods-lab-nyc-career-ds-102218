import pytest
from driver import Driver

def test_driver_class_init():
    driver_1 = Driver("Terrance", "Toyota", "Camry")
    driver_2 = Driver("Rachel", "Subaru", "Forrester")
    driver_3 = Driver("Jeff", "Toyota", "Camry")
    driver_4 = Driver("Lore", "Honda", "Pilot")
    assert Driver._all == [driver_1, driver_2, driver_3, driver_4]
    assert Driver._count == 4

def test_fleet_size_class_method():
    assert Driver.fleet_size() == 4

def test_driver_names_class_method():
    assert Driver.driver_names() == ["Terrance", "Rachel", "Jeff", "Lore"]

def test_fleet_makes_class_method():
    assert Driver.fleet_makes() == ["Toyota", "Toyota", "Subaru", "Honda"]

def test_fleet_models_class_method():
    assert Driver.fleet_models() == ["Camry", "Camry", "Forrester", "Pilot"]

def test_fleet_makes_count_class_method():
    assert Driver.fleet_makes_count() == {'Honda': 1, 'Toyota': 2, 'Subaru': 1}

def test_fleet_models_count_class_method():
    assert Driver.fleet_models_count() == {'Pilot': 1, 'Camry': 2, 'Forrester': 1}

def test_percent_of_fleet_class_method():
    assert Driver.percent_of_fleet("Toyota") == "50.0%"
