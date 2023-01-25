from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self):
        pass
    def needs_service(self, last_service_date):
        return 