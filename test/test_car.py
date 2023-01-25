import unittest
from datetime import datetime

from battery import spinder_battery
from battery import nubbin_battery

from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

import car

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0


        battery = spinder_battery()
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())




    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        battery = spinder_battery()
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())


    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        battery = spinder_battery()
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        battery = spinder_battery()
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = spinder_battery()
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())
        

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        battery = spinder_battery()
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        battery = spinder_battery()
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        battery = spinder_battery()
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())


        battery = spinder_battery()
        engine = sternman_engine(warning_light_is_on)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())


    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        battery = spinder_battery()
        engine = sternman_engine(warning_light_is_on)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        battery = spinder_battery()
        engine = sternman_engine(warning_light_is_on)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        battery = spinder_battery()
        engine = sternman_engine(warning_light_is_on)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

        battery = nubbin_battery()
        engine = willoughby_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())


    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = nubbin_battery()
        engine = willoughby_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        battery = nubbin_battery()
        engine = willoughby_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        battery = nubbin_battery()
        engine = willoughby_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0


        battery = nubbin_battery()
        engine = capulet_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = nubbin_battery()
        engine = capulet_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        battery = nubbin_battery()
        engine = capulet_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        battery = nubbin_battery()
        engine = capulet_engine(current_mileage, last_service_date)

        car = car(engine, battery)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
