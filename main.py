from warrior import Warrior
from Weapon import Weapon
from Shield import Shield

import random

name1 = "The best of the best"
name2 = "Superhero"

warrior1 = Warrior(name1, 100, Weapon("hero's weapon", 2, 6), Shield("hero's shield", 70, (10, 20)))
warrior2 = Warrior(name2, 100, Weapon("superhero's weapon", 2, 6), Shield("superhero's shield", 70, (10, 20)))

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