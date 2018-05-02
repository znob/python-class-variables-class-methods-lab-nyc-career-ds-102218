
# Python Class Variables and Class Methods Lab

## Introduction
In this lab, we are going to put our skills to the test by creating class methods and class variables that will help our program remember instance objects and allow us to operate on these objects in interesting ways. We will be working with a Driver class, which we can define in our file, `driver.py`.

## Objectives
* Use class variables to keep track of data pertaining to a class
* Define class methods that expose data pertaining to a class

## Instructions

Okay, so, we have a fleet drivers and we want to be able to make queries to get details about our drivers. So, our Driver class should have two class variables; `_all` and `_count`. The `_all` class variable should be assigned to a list that keeps track of all instance objects for the Driver class. The `_count` class variable should keep track of the number of drivers in our fleet. Initially, we wont have any drivers, so, it should be set to `0`.

> **note:** remember to load the autoreload extension from IPython
```python
%load_ext autoreload
%autoreload 2
```


```python
from driver import Driver
```

We want our drivers to have the following attributes; name, car make, and car model. Again, by convention these attributes should have a leading underscore and be snakecased where appropriate. We will also want to define instance methods using the appropriate decorator to read (get) all of these attributes.


```python
driver_one = Driver("Helga Pataki", "Toyota", "Camry")
```

Great! Now, onto the more fun stuff. Let's create a few different instance methods that will help us answer questions like how many drivers do we currently have in our fleet? What percent of drivers drive a Toyota and of that, how many drive a Camry? Or more generally, which car make/model cars do our drivers drive?

To do this, our class will need to have the two class varibles we mentioned earlier, `_all` and `_count`, as well as the class methods listed below:


```python
Driver.fleet_size() # returns the number of drivers in the fleet
# example: 10
```


```python
Driver.driver_names() # returns a list of driver names as strings
# example: ["Anna", "Jeff", "Carol", "Guillaume"]
```


```python
Driver.fleet_makes() # returns a list of names car makes in the fleet
# example: ["Toyota", "Jeep", "Honda", "Kia"]
```


```python
Driver.fleet_models() # returns a list of names car models in the fleet
# example: ["Camry", "Highlander", "Wrangler", "Civic"]
```


```python
Driver.fleet_make_count() # returns a list of dictionaries car makes in the fleet
# example: [{"Toyota": 8}, {"Jeep": 2}, {"Honda": 9,} {"Kia": 6}]
```

Then, let's write a class method with the `@classmethod` decorator and name it `save`. Remember, in order to reference the class, we use the parametere `cls` in our method definition in place of `self`. The `save` class method will also need to know what it is saving, so, the second argument will be the instance object we are appending to our `_all` list. Once the instance object is added to our list, it should return the newly updated `_all` list.


```python
Car.save(new_car) # [<__main__.Car object at 0x1068dd7f0>]
```

## Summary

