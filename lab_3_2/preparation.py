from abc import ABC


class Preparation(ABC):
    def __init__(self, milk: float, water: float,
                 sugar: float, coke: float, liquidCoffee: float,
                 addedFlavour: float, tea: float):
        self.milk = milk
        self.water = water
        self.sugar = sugar
        self.coke = coke
        self.liquidCoffee = liquidCoffee
        self.addedFlavour = addedFlavour
        self.tea = tea
