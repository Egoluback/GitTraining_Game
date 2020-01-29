class Warrior:
    def __init__(self, name: str, hp: int, weapon, shield):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.shield = shield
        self.IsAlive = True

    def ChangeHp(self, x):
        self.hp += x
        if self.hp <= 0:
            self.IsAlive = False
        return self.IsAlive

    def Attack(self, enemy):
        damage = self.weapon.GetDamage()
        damage -= enemy.shield.GetDefense()
        if damage < 0: damage = 0
        has_killed = not enemy.ChangeHp(-damage)
        return has_killed

    def GetHp(self):
        return self.hp

    def GetName(self):
        return self.name
