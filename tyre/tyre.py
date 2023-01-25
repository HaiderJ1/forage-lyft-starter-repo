from abc import ABC, abstractmethod

class Tyre(ABC):
    def __init__(self, tyre_wear):
        pass

    @abstractmethod
    def needs_service(tyre_array):
        pass
