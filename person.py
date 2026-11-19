from bow import Bow
from sword import Sword


class Person:
    def __init__(self, name):
        self.__name = name
        self.__bow = None
        self.__sword = None

    def get_name(self) -> str:
        return self.__name

    def collect_weapon(self, weapon):
        if isinstance(weapon, Bow):
            self.__bow = weapon
        elif isinstance(weapon, Sword):
            self.__sword = weapon

    def bow_attack(self) -> None:
        if hasattr(self.__bow, "attack"):
            print(self.__bow.attack())
        else:
            print(f"У лука нет метода attack()")

    def get_bow_arrows(self) -> None:
        print(self.__bow.get_arrows_count())

    def sword_attack(self) -> None:
        if hasattr(self.__sword, "attack"):
            print(self.__sword.attack())
        else:
            print(f"У меча нет метода attack()")

    def get_sword_sharpness(self) -> None:
        print(self.__sword.get_wear_resistance())
