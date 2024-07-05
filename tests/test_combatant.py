from src.models import (
	Alignment, Combatant
)


COMBATANT_NAME = 'Nathan'
COMBATANT_ALIGNMENT = Alignment.GOOD


def combatant_setup() -> Combatant:
	combatant = Combatant(
		name=COMBATANT_NAME,
		alignment=COMBATANT_ALIGNMENT,
	)
	return combatant


def test_combatant_armor_class():
	"""
	Test case for Combatant armor_class getter and setter
	"""
	combatant = combatant_setup()
	combatant.armor_class = 20
	assert combatant.armor_class == 20


def test_combatant_armor_class_default():
	"""
	Test case for Combatant armor_class default value
	"""
	combatant = combatant_setup()
	assert combatant.armor_class == 10


def test_combatant_hit_points():
	"""
	Test case for Combatant hit_points getter and setter
	"""
	combatant = combatant_setup()
	combatant.hit_points = 20
	assert combatant.hit_points == 20


def test_combatant_hit_points_default():
	"""
	Test case for Combatant hit_points default value
	"""
	combatant = combatant_setup()
	assert combatant.hit_points == 5
