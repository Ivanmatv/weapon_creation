from bow import Bow
from sword import Sword
from person import Person


person = Person("Иван")
bow = Bow(10)
sword = Sword(100)

weapons = [bow, sword]

def add_weapon(weapon):
    person.collect_weapon(weapon)

for weapon in weapons:
    add_weapon(weapon)

person.get_name()

person.sword_attack()
person.get_sword_sharpness()

person.bow_attack()
person.get_bow_arrows()
