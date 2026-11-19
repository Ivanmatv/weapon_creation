class Sword:
    def __init__(self, wear_resistance: int) -> None:
        self.__wear_resistance: int = wear_resistance

    def attack(self) -> str:
        if self.__wear_resistance > 0:
            self.__wear_resistance -= 10
            return "Атака мечом"

        return "Мечь затуплен"

    def get_wear_resistance(self) -> int:
        return self.__wear_resistance