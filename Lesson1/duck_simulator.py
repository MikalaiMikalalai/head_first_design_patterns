######################################################
#                 Strategy                           #
######################################################

import abc

######################################################
#                 Fly Behaviours                     #
######################################################


class FlyBehaviour(abc.ABC):
    """Abstract superclass."""
    @abc.abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehaviour):
    """Real ducks that can fly."""
    def fly(self):
        print("I'm flying high!")


class FlyNoWay(FlyBehaviour):
    """Artificial ducks can't fly."""
    def fly(self):
        print("I can't fly, but you can take me"
              " with you to the bath and have fun.")


######################################################
#                 Quack Behaviours                   #
######################################################

class QuackBehaviour(abc.ABC):
    """Abstract superclass."""
    @abc.abstractmethod
    def quack(self):
        pass


class Quack(QuackBehaviour):
    """Duck quacks."""
    def quack(self):
        print("Quack!!!")


class Squeak(QuackBehaviour):
    """Duck squeak."""
    def quack(self):
        print("Squeak!!!")


class MuteDuck(QuackBehaviour):
    """Do nothing."""
    def quack(self):
        print('Complete silence.')


######################################################
#                      Ducks                         #
######################################################

class Duck(abc.ABC):
    """Duck abstract superclass."""
    def set_quack_behaviour(self, quack_behaviour):
        self.quack_behaviour = quack_behaviour

    def set_fly_behaviour(self, fly_behaviour):
        self.fly_behaviour = fly_behaviour

    def perform_quack(self):
        self.quack_behaviour.quack()

    def perform_fly(self):
        self.fly_behaviour.fly()

    def swim(self):
        print("I'm swimming!")

    @abc.abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behaviour = Quack()
        self.fly_behaviour = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck.")


class RubberDuck(Duck):
    def __init__(self):
        self.quack_behaviour = Squeak()
        self.fly_behaviour = FlyNoWay()

    def display(self):
        print("I'm a cool Rubber duck.")


if __name__ == "__main__":
    mallard_duck = MallardDuck()
    mallard_duck.perform_quack()
    mallard_duck.perform_fly()
    mallard_duck.display()

    rubber_duck = RubberDuck()
    rubber_duck.perform_quack()
    rubber_duck.perform_fly()
    rubber_duck.display()
