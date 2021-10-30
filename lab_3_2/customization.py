from abc import ABC


class Customization(ABC):
    def __init__(self, extraMilk: float, sugar: float, mugSize: float):
        self.extraMilk = extraMilk
        self.sugar = sugar
        self.mugSize = mugSize
