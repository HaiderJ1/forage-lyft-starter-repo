import unittest
from datetime import datetime

from battery.spinder_battery import SpindlerBattery
from battery.nubbin_battery  import NubbinBattery


from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre

from car import Car

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre
        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())




    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery,tyre, tyre_array)  
        self.assertFalse(car.needs_service())


    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())
        

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre


        battery = SpindlerBattery(today, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())


    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = SpindlerBattery(today, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

       

        battery = NubbinBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())


    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = NubbinBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = NubbinBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = NubbinBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre


        battery = NubbinBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = NubbinBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = NubbinBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery, tyre, tyre_array)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tyre_array = [0,0,0,0]

        tyre = CarriganTyre

        battery = NubbinBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        car = Car(engine, battery,tyre, tyre_array)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
