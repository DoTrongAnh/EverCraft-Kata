from enum import Enum


class Alignment(Enum):
	GOOD = 'good'
	EVIL = 'evil'
	NEUTRAL = 'neutral'


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

	def __init__(self, **kwargs):
		super(self).__init__(**kwargs)
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
