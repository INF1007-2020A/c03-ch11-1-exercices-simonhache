"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	def __init__(self, name, power, min_level):
		self.__name__ = name
		self.power = power
		self.min_level = min_level

	def make_unarmed(self):
		UNARMED_POWER = 20
		self.__name__ = "Unarmed"
		self.power = UNARMED_POWER
		self.min_level = 0

class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.current_hp = max_hp

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts

	crit = random.choice(range(16))
	if crit == 1:
		crit = 2
	else:
		crit = 1
	random_crit = ((random.random() * 15) + 85)/100

	modifier = crit * random_crit
	first_el = ((2 * attacker.level) / 5) + 2
	damage = ((first_el * attacker.weapon.power * (attacker.attack/defender.defense))/50) + 2
	damage *= modifier
	damage = int(damage)
	print(f"{attacker.name} used {attacker.weapon.__name__}")
	if crit == 2:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")
	defender.current_hp -= damage


def run_battle(c1, c2):
	# Initialisation du combat
	attacker = c1
	defender = c2
	turn = 0

	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		turn += 1
		deal_damage(attacker, defender)

		if defender.current_hp <=0:
			print(f"{defender.name } is sleeping with the fishes.")
			break

		attacker, defender = defender, attacker

	return turn
