from warrior.py import Warrior
from weapon.py import Weapon
from Shield.py import Shield

import random

name1 = "The best of the best"
name2 = "Superhero"

warrior1 = Warrior(name1, 100, Weapon("hero's weapon", 10, 10), Shield("hero's shield", 70, (10, 40)))
warrior2 = Warrior(name2, 100, Weapon("superhero's weapon", 10, 10), Shield("superhero's shield", 70, (10, 40)))

anyoneAlive = True

while anyoneAlive:
    prHp = warrior2.GetHp()
    anyoneAlive = not warrior1.Attack(warrior2)
    nowHp = warrior2.GetHp()
    print(name1 + " нанес удар в размере " + str(prHp - nowHp))
    
    prHp = warrior1.GetHp()
    anyoneAlive = not warrior2.Attack(warrior1)
    nowHp = warrior1.GetHp()
    print(name1 + " нанес удар в размере " + str(prHp - nowHp))