from bow import Bow
from sword import Sword


class Person:
    def __init__(self, name):
        self.name = name
        self.bow = Bow()
        self.sword = Sword()

    def sword_attack(self) -> None:
        print(self.sword.attack())

    def bow_attack(self) -> None:
        print(self.bow.attack())
