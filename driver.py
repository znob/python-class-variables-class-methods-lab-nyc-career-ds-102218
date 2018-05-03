class Driver:

    _all = []
    _count = 0

    def __init__(self, name, make, model):
        self._name = name
        self._car_make = make
        self._car_model = model
        Driver.increment_count()
        Driver.save(self)

    @property
    def name(self):
        return self._name

    @property
    def car_make(self):
        return self._car_make

    @property
    def car_model(self):
        return self._car_model

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def count(cls):
        return cls._count

    @classmethod
    def save(cls, driver):
        cls.all().append(driver)
        return cls.all()

    @classmethod
    def increment_count(cls):
        cls._count += 1
        return cls.count()

    @classmethod
    def fleet_size(cls):
        return cls.count()

    @classmethod
    def driver_names(cls):
        names = [getattr(driver, "name") for driver in cls.all()]
        return names

    @classmethod
    def get_fleet_attr(cls, attr):
        return [getattr(driver, attr) for driver in cls.all()]

    @classmethod
    def fleet_makes(cls):
        return cls.get_fleet_attr("car_make")

    @classmethod
    def fleet_models(cls):
        return cls.get_fleet_attr("car_model")

    @classmethod
    def make_histogram(cls, list):
        new_histogram = {}
        for name in list:
            if name in new_histogram:
                new_histogram[name] += 1
            else:
                new_histogram[name] = 1
        return new_histogram

    @classmethod
    def fleet_makes_count(cls):
        fleet_makes = cls.fleet_makes()
        fleet_makes_histogram = cls.make_histogram(fleet_makes)
        return fleet_makes_histogram

    @classmethod
    def fleet_models_count(cls):
        fleet_models = [getattr(driver, "car_model") for driver in cls.all()]
        fleet_models_histogram = cls.make_histogram(fleet_models)
        return fleet_models_histogram

    @classmethod
    def percent_of_make(cls, make):
        fleet_makes_histogram = cls.fleet_makes_count()
        fleet_count_list = fleet_makes_histogram.values()
        total = sum(list(fleet_count_list))
        make_frequency = fleet_makes_histogram[make]
        percent = float((make_frequency/total)*100)
        return str(percent) + "%"
