import machine
from rollingFilter import RollingFilter

class PressureSensor:
    def __init__(self, sensorPin: int):
        self.sensorPin = sensorPin
        self.lowerBound = 0
        self.upperBound = 65535
        self.sensor = machine.ADC(sensorPin)
        self.range = self.upperBound - self.lowerBound
        self.previousRead = 0
        self.rollingFilter = RollingFilter(20)

    def setBand(self, lowerBound, upperBound):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.range = self.upperBound - self.lowerBound

    def read16(self):
        return self.sensor.read_u16()

    def getPreviousRead(self):
        return int(self.previousRead)

    def read80(self):
        read = self.rollingFilter.filter(self.read16())
        read = read - self.lowerBound
        read = (read / self.range) * 80
        self.previousRead = read
        return int(read)