from datetime import datetime
from battery.battery import Battery
from yearCalc import add_years_to_date


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date
        service_threshold_date = add_years_to_date(service_threshold_date, 2)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False