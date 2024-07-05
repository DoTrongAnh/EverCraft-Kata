from enum import Enum
import random


class Alignment(Enum):
	GOOD = 'good'
	EVIL = 'evil'
	NEUTRAL = 'neutral'


class Dice:
	sides = list(range(1, 21))

	@classmethod
	def roll(cls):
		return random.choice(cls.sides)


class Character:
    _name: str
    _alignment: Alignment

    def __init__(self, **kwargs):
        self._name = kwargs.get('name', '')
        self._alignment = kwargs.get('alignment', Alignment.NEUTRAL)

    @property
    def name(self):
    	return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def alignment(self):
    	return self._alignment

    @alignment.setter
    def alignment(self, alignment: Alignment):
    	self._alignment = alignment


class Combatant(Character):
	_armor_class: int
	_hit_points: int
	_is_alive: bool = True

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self._armor_class = kwargs.get('armor_class', 10)
		self._hit_points = kwargs.get('hit_points', 5)

	@property
	def armor_class(self):
		return self._armor_class

	@armor_class.setter
	def armor_class(self, armor_class: int):
		self._armor_class = armor_class

	@property
	def hit_points(self):
		return self._hit_points

	@hit_points.setter
	def hit_points(self, hit_points: int):
		self._hit_points = hit_points

	@property
	def is_alive(self):
		return self._is_alive

	def take_damage(self, damage: int):
		self._hit_points = max(self._hit_points - damage, 0)
		if self._hit_points <= 0:
			self._is_alive = False

	def attack(self, opponent):
		dice_roll = Dice.roll()
		damage = 0
		if dice_roll == 20 or dice_roll >= opponent.armor_class:
			damage = 1
		if dice_roll == 20:
			damage *= 2
		if damage:
			opponent.take_damage(damage)
