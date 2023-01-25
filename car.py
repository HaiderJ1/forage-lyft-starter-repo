from abc import ABC

import datetime
from serviceable import Serviceable


from battery.spinder_battery import SpindlerBattery
from battery.nubbin_battery  import NubbinBattery
from battery.battery import Battery



class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery


    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()


        
