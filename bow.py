class Bow:
    def __init__(self, arrows_count: int) -> None:
        self.__arrows_count: int = arrows_count

    def attack(self) -> str:
        if self.__arrows_count > 0:
            self.__arrows_count -= 1
            return "Атака из лука"

        return "Стрелы закончились"

    def get_arrows_count(self) -> int:
        return self.__arrows_count
