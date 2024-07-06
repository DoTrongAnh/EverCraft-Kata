from enum import Enum
import random


class Ability:
	modifiers = {
		1: -5,
		2: -4,
		3: -4,
		4: -3,
		5: -3,
		6: -2,
		7: -2,
		8: -1,
		9: -1,
		10: 0,
		11: 0,
		12: 1,
		13: 1,
		14: 2,
		15: 2,
		16: 3,
		17: 3,
		18: 4,
		19: 4,
		20: 5,
	}

	@classmethod
	def set_ability(cls, value):
		return min(20, max(1, value))

	@classmethod
	def get_modifier(cls, value):
		return cls.modifiers.get(value, 0)


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
    _strength: int
    _dexterity: int
    _constitution: int
    _wisdom: int
    _intelligence: int
    _charisma: int
    _experience: int = 0
    _level: int = 1

    def __init__(self, **kwargs):
        self._name = kwargs.get('name', '')
        self._alignment = kwargs.get('alignment', Alignment.NEUTRAL)
        self._strength = Ability.set_ability(kwargs.get('strength', 10))
        self._dexterity = Ability.set_ability(kwargs.get('dexterity', 10))
        self._constitution = Ability.set_ability(kwargs.get('constitution', 10))
        self._wisdom = Ability.set_ability(kwargs.get('wisdom', 10))
        self._intelligence = Ability.set_ability(kwargs.get('intelligence', 10))
        self._charisma = Ability.set_ability(kwargs.get('charisma', 10))

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

    @property
    def strength(self):
    	return self._strength

    @strength.setter
    def strength(self, value):
    	self._strength = Ability.set_ability(value)

    @property
    def dexterity(self):
    	return self._dexterity

    @dexterity.setter
    def dexterity(self, value):
    	self._dexterity = Ability.set_ability(value)

    @property
    def constitution(self):
    	return self._constitution

    @constitution.setter
    def constitution(self, value):
    	self._constitution = Ability.set_ability(value)

    @property
    def wisdom(self):
    	return self._wisdom

    @wisdom.setter
    def wisdom(self, value):
    	self._wisdom = Ability.set_ability(value)

    @property
    def intelligence(self):
    	return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
    	self._intelligence = Ability.set_ability(value)

    @property
    def charisma(self):
    	return self._charisma

    @charisma.setter
    def charisma(self, value):
    	self._charisma = Ability.set_ability(value)

    @property
    def experience(self):
    	return self._experience

    @property
    def level(self):
    	return self._level
    

    def gain_exp(self, value):
    	EXP_PER_LEVEL = 1000
    	old_exp  = self._experience
    	self._experience += value
    	if value > 0:
    		for _ in range(old_exp // EXP_PER_LEVEL, self._experience // EXP_PER_LEVEL):
    			self.level_up()

    def level_up(self):
    	self._level += 1


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
		return self._armor_class + Ability.get_modifier(self._dexterity)

	@armor_class.setter
	def armor_class(self, armor_class: int):
		self._armor_class = armor_class

	@property
	def hit_points(self):
		if self._hit_points >= 0 and - Ability.get_modifier(self._constitution) >= self._hit_points:
			return 1
		return self._hit_points + Ability.get_modifier(self._constitution)

	@hit_points.setter
	def hit_points(self, hit_points: int):
		self._hit_points = hit_points

	@property
	def is_alive(self):
		return self._is_alive

	def take_damage(self, damage: int):
		# Ensure the Combatant is not healed or overkilled
		self._hit_points -= damage
		if self.hit_points <= 0:
			self._is_alive = False

	def attack(self, opponent):
		dice_roll = Dice.roll()
		damage = 0
		# Check if original roll is a crit
		crit = dice_roll == 20
		mod = Ability.get_modifier(self._strength)
		# Add original modifier to dice roll
		dice_roll += mod
		if crit or dice_roll >= opponent.armor_class:
			damage = 1 + self._level // 2
		# Double damage and modifier when crit
		if crit:
			damage *= 2
			mod *= 2
		# If damage is 0, attack misses and modifier does nothing
		if damage:
			damage = max(1, damage + mod)
			opponent.take_damage(damage)
			self.gain_exp(10)

	def level_up(self):
		super().level_up()
		self._hit_points += 5
