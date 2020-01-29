import random


class Weapon():
	def __init__(self, name, dices, edges):
		self.name = name
		self.dices = dices
		self.edges = edges

	def getname(self):
		return self.name

	def GetDamage(self):
		res = 0
		for i in range(0, self.dices):
			res += random.randint(1, self.edges + 1)
			return res
