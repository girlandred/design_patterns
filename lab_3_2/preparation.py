from abc import ABC


class Preparation(ABC):
    """
        Represents abstract class Customization

        ...

        Attributes
        ----------
        milk : float
            milk
        water : float
            water presence
        sugar : float
            presence of sugar
        coke : float
            instance of coke
        liquidCoffee : float
            coffee liquid
        addedFlavour : float
            flavour
        tea : float
            tea
    """

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
