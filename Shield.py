import random


class Shield:
    def __init__(self, name, chance, defrange):
        self.name = name
        self.chance = chance
        self.defrange = defrange

    def getName(self):
        return self.name

    def GetDefense(self):
        result = 0
        number = random.randint(1, 101)
        if (number < self.chance):
            result = random.randint(self.defrange[0], self.defrange[1] + 1)
        return result
