class RollingFilter:
    def __init__(self, windowSize: int):
        self.windowSize = windowSize
        self.table = [0] * windowSize
        self.index = 0
        self.sum = 0

    def filter(self, value: int):
        self.sum -= self.table[self.index]
        self.sum += value
        self.table[self.index] = value
        self.index += 1
        if self.index == self.windowSize:
            self.index = 0
        return self.sum / self.windowSize