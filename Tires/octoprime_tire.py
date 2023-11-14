from .tire import tire

class octoprime(tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        sensor_sum = 0
        for sensor in self.sensors:
            sensor_sum += sensor
        return sensor_sum >= 3