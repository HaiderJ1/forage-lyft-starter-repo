from tyre.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__ (self, tyre_wear):
        self.tyre_wear = tyre_wear  
    def needs_service(tyre_array):
        for value in tyre_array:
            if value >= 0.9:
                return True
        return False