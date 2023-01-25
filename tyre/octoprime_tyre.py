from tyre.tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__ (self, tyre_wear):
        self.tyre_wear = tyre_wear
    def needs_service(tyre_array):
        total = 0
        for value in tyre_array:
            total = total + value
        if total > 3:
            return True
        return False