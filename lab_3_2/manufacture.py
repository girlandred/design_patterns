from abc import ABC, abstractmethod

from customization import Customization
from preparation import Preparation


class ProductFactory(ABC):
    """
    Represents abstract ProductFactory class

    ...

    Methods:
    --------
        get_product(customization)

        get_product_factory()

    """

    @abstractmethod
    def get_product(self, customization):
        pass

    @staticmethod
    def get_product_factory():
        pass


class CappuccinoFactory(ProductFactory):
    """
        Represents class CappuccinoFactory

        ...

        Methods
        ----------
        get_product(customization):
            Creating Cappuccino.
    """

    def get_product(self, customization):
        return Cappuccino()


class BlackCoffeeFactory(ProductFactory):
    """
        Represents class BlackCoffeeFactory

        ...

        Methods
        ----------
        get_product(customization):
            Creating BlackCoffee.
    """

    def get_product(self, customization):
        return BlackCoffee()


class LemonadeFactory(ProductFactory):
    """
        Represents class LemonadeFactory

        ...

        Methods
        ----------
        get_product(customization):
            Creating Lemonade.
    """

    def get_product(self, customization):
        return Lemonade()


class HotMilkFactory(ProductFactory):
    """
        Represents class HotMilkFactory

        ...

        Methods
        ----------
        get_product(customization):
            Creating HotMilk.
    """

    def get_product(self, customization):
        return HotMilk()


class CocaColaFactory(ProductFactory):
    """
        Represents class CocaColaFactory

        ...

        Methods
        ----------
        get_product(customization):
            Creating CocaCola.
    """

    def get_product(self, customization):
        return CocaCola()


class Cappuccino(CappuccinoFactory):
    """
        Represents class Cappuccino

        ...

        Methods
        ----------
        preparation(preparation: Preparation):
            Process of creation cappuccino.
        customization(customization: Customization):
            Drinks customization.
        make():
            Creating drink.
        set_milk():
            Adding milk.
        set_sugar():
            Adding sugar in drink.
        set_coffee():
            Setting coffee in drink.
    """

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
    """
        Represents class BlackCoffee

        ...

        Methods
        ----------
        preparation(preparation: Preparation):
            Process of creation Black Coffee.
        customization(customization: Customization):
            Drinks customization.
        make():
            Creating drink.
        set_water():
            Setting watter.
        set_coffee():
            Setting coffee in drink.
    """

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
    """
            Represents class Lemonade

            ...

            Methods
            ----------
            preparation(preparation: Preparation):
                Process of creation lemonade.
            customization(customization: Customization):
                Drinks customization.
            make():
                Creating drink.
            set_water():
                Setting watter.
            set_sugar():
                Adding sugar in drink.
            set_lemon_juice():
                Setting lemon juice in lemonade.
        """

    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def set_water(self):
        print('Water in ', type(self).__name__, 'set')

    def set_sugar(self):
        print('A lot of sugar was set in', type(self).__name__)

    def set_lemon_juice(self):
        print('When life gives you lemons, make', type(self).__name__)


class HotMilk(HotMilkFactory):
    """
        Represents class HotMilk

        ...

        Methods
        ----------
        preparation(preparation: Preparation):
            Process of creation Hot Milk.
        customization(customization: Customization):
            Drinks customization.
        make():
            Creating drink.
        set_milk():
            Adding milk.
    """

    def preparation(self, preparation: Preparation):
        pass

    def customization(self, customization: Customization):
        pass

    def make(self):
        print(type(self).__name__, 'was made!')

    def set_milk(self):
        print('Hot milk was set in', type(self).__name__)


class CocaCola(CocaColaFactory):
    """
            Represents class CocaCola

            ...

            Methods
            ----------
            preparation(preparation: Preparation):
                Process of creation Coca - Cola.
            customization(customization: Customization):
                Drinks customization.
            make():
                Creating drink.
            set_water():
                Setting watter.
            set_coke():
                Setting coke in coca - cola.
        """

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
