from abc import ABC

import datetime
from serviceable import Serviceable


from battery.spinder_battery import SpindlerBattery
from battery.nubbin_battery  import NubbinBattery
from battery.battery import Battery
from tyre.tyre import Tyre



class Car(Serviceable):
    def __init__(self, engine, battery, tyre, tyre_array):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre
        self.tyre_array = tyre_array

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tyre.needs_service(self.tyre_array)


        
