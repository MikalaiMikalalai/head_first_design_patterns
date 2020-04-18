######################################################
#            Classic Decorator                       #
######################################################

import abc

######################################################
#                   Interfaces                       #
######################################################


class Beverage(abc.ABC):

    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abc.abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage, abc.ABC):

    @abc.abstractmethod
    def get_description(self):
        pass

######################################################
#                   Implementations                  #
######################################################


class Espresso(Beverage):

    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return .89


class DarkRoast(Beverage):

    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return 1.20


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + .20


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Wheep"

    def cost(self):
        return self.beverage.cost() + .12


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + .32


if __name__ == '__main__':

    beverage = Espresso()
    print(f'{beverage.get_description()} ${beverage.cost()}')

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f'{beverage2.get_description()} ${beverage2.cost()}')

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f'{beverage3.get_description()} ${beverage3.cost()}')
