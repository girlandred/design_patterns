from abc import ABC

from manufacture import CocaColaFactory
from customization import Customization


class ProductStore(ABC):
    def __init__(self):
        pass

    def make_product(self):
        for factory in [CocaColaFactory()]:
            self.factory = factory
            self.CocaCola = self.factory.get_product(customization=Customization)
            self.CocaCola.make()
            self.CocaCola.set_water()
            self.CocaCola.set_coke()


product = ProductStore()
product.make_product()
