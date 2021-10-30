from abc import ABC, abstractmethod
from customization import Customization
from preparation import Preparation


class ProductFactory(ABC):

    @abstractmethod
    def get_product(self, customization):
        pass

    @staticmethod
    def get_product_factory():
        pass


class CappuccinoFactory(ProductFactory):
    def get_product(self, customization):
        return Cappuccino()


class BlackCoffeeFactory(ProductFactory):
    def get_product(self, customization):
        return BlackCoffee()


class LemonadeFactory(ProductFactory):
    def get_product(self, customization):
        return Lemonade()


class HotMilkFactory(ProductFactory):
    def get_product(self, customization):
        return HotMilk()


class CocaColaFactory(ProductFactory):
    def get_product(self, customization):
        return CocaCola()


class Cappuccino(CappuccinoFactory):

    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def set_milk(self):
        print('Steamed milk foam was set in', type(self).__name__)

    def set_sugar(self):
        print('Some sugar was set in', type(self).__name__)

    def set_coffee(self):
        print('Some coffee was added in', type(self).__name__)


class BlackCoffee(BlackCoffeeFactory):
    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def set_water(self):
        print('Water was set in', type(self).__name__)

    def set_coffee(self):
        print('A lot of coffee was added in', type(self).__name__)


class Lemonade(LemonadeFactory):
    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    @staticmethod
    def set_water():
        print('Water was set')

    def set_sugar(self):
        print('A lot of sugar was set in', type(self).__name__)

    def set_lemon_juice(self):
        print('When life gives you lemons, make', type(self).__name__)


class HotMilk(HotMilkFactory):
    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def set_milk(self):
        print('Hot milk was set in', type(self).__name__)


class CocaCola(CocaColaFactory):
    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def set_water(self):
        print('Water was set in', type(self).__name__)

    def set_coke(self):
        print('Secret ingredient was added in', type(self).__name__)
