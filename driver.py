class Driver:
    _all = []
    _count = 0

    def __init__(self, name, car_make, car_model):
        self.name = name
        self.car_make = car_make
        self.car_model = car_model
        Driver._all.append(self)
        Driver._count += 1

    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names(cls):
        names = list(map(lambda driver: driver.name, cls._all))
        return names

    @classmethod
    def fleet_makes(cls):
        car_makes = list(map(lambda driver: driver.car_make, cls._all))
        return car_makes

    @classmethod
    def fleet_models(cls):
        car_models = list(map(lambda driver: driver.car_model, cls._all))
        return car_models

    @classmethod
    def fleet_makes_count(cls):
        makes_histo = {}
        for driver in cls._all:
            if driver.car_make in makes_histo:
                makes_histo[driver.car_make] += 1
            else:
                makes_histo[driver.car_make] = 1
        return makes_histo

    @classmethod
    def fleet_models_count(cls):
        models_histo = {}
        for driver in cls._all:
            if driver.car_model in models_histo:
                models_histo[driver.car_model] += 1
            else:
                models_histo[driver.car_model] = 1
        return models_histo

    @classmethod
    def percent_of_fleet(cls, make):
        fleet = cls.fleet_makes()
        fleet_count = len(fleet)
        makes_count = cls.fleet_makes_count()
        num = float((makes_count[make]/fleet_count)*100)
        num_string = str(num)
        percent = num_string + "%"
        return percent
