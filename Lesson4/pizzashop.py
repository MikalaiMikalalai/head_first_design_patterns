######################################################
#                      Factory                       #
######################################################

import abc

######################################################
#                   Interfaces                       #
######################################################


class Dough(abc.ABC):
    pass


class Sauce(abc.ABC):
    pass


class Veggies(abc.ABC):
    pass


class Cheese(abc.ABC):
    pass


class Pepperoni(abc.ABC):
    pass


class Clams(abc.ABC):
    pass


class PizzaIngredientFactory(abc.ABC):
    @abc.abstractmethod
    def create_dough(self):
        pass

    @abc.abstractmethod
    def create_sauce(self):
        pass

    @abc.abstractmethod
    def create_cheese(self):
        pass

    @abc.abstractmethod
    def create_veggies(self):
        pass

    @abc.abstractmethod
    def create_pepperoni(self):
        pass

    @abc.abstractmethod
    def create_clam(self):
        pass


class Pizza(abc.ABC):

    def __init__(self):
        self.name:  str
        self.dough: Dough
        self.sauce: Sauce
        self.cheese: Cheese
        self.pepperoni: Pepperoni
        self.clam: Clams
        self.toppings = []
        self.veggies = []

    @abc.abstractmethod
    def prepare(self):
        print(f'Preparing {self.name}')
        print(f'Tossing dough...')
        print(f'Adding sauce...')
        print(f'Adding toppings:')
        for topping in self.toppings:
            print(f'  - {topping}')

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class PizzaStore(abc.ABC):

    def order_pizza(self, pizza_type):

        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abc.abstractmethod
    def create_pizza(self, pizza_type):
        pass

######################################################
#                   Implementations                  #
######################################################


class ThinCrustDough(Dough):
    pass


class ThickCrustDough(Dough):
    pass


class MarinaraSauce(Sauce):
    pass


class PlumTomatoSauce(Sauce):
    pass


class ReggianoCheese(Cheese):
    pass


class MozzarellaCheese(Cheese):
    pass


class SlicedPepperoni(Pepperoni):
    pass


class FreshClams(Clams):
    pass


class FrozenClams(Clams):
    pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return ["Garlic", "Onion", "Mushroom", "RedPepper"]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return ["Garlic", "Onion", "Mushroom", "RedPepper"]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.get_name()}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.get_name()}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class NYPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("NY Style Sauce and Cheese Pizza")
        # elif pizza_type == 'pepperoni':
        #     pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("NY Style Clam Pizza")
        # elif pizza_type == 'veggie':
        #     pizza = VeggiePizza()

        return pizza


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")
        # elif pizza_type == 'pepperoni':
        #     pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")
        # elif pizza_type == 'veggie':
        #     pizza = VeggiePizza()

        return pizza


if __name__ == '__main__':
    ny_pizza_store = NYPizzaStore()
    chicago_pizza_store = ChicagoPizzaStore()

    pizza = ny_pizza_store.order_pizza('cheese')
    print(f'Ethan ordered a {pizza.get_name()}\n')

    pizza = chicago_pizza_store.order_pizza('cheese')
    print(f'Joel ordered a {pizza.get_name()}\n')
