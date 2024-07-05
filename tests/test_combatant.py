import pytest

from src.models import (
	Ability, Alignment, Combatant
)


COMBATANT_NAME = 'Nathan'
COMBATANT_ALIGNMENT = Alignment.GOOD
ENEMY_NAME = 'Foe'
ENEMY_ALIGHMENT = Alignment.EVIL


def combatant_setup() -> Combatant:
	combatant = Combatant(
		name=COMBATANT_NAME,
		alignment=COMBATANT_ALIGNMENT,
	)
	return combatant


def opponent_setup() -> Combatant:
	opponent = Combatant(
		name=ENEMY_NAME,
		alignment=ENEMY_ALIGHMENT,
	)
	return opponent


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


@pytest.mark.parametrize(
	'dice_roll, expected_damage',
	[
		(9, 0),  # Attack should miss
		(10, 1),  # Attack should hit
		(20, 2),  # Attack should crit
	]
)
def test_combatant_attack(mocker, dice_roll, expected_damage):
	"""
	Test case for Combatant attack with various rolls
	"""
	combatant = combatant_setup()
	opponent = opponent_setup()
	mocker.patch('src.models.Dice.roll', return_value=dice_roll)
	opponent_init_hp = opponent.hit_points
	combatant.attack(opponent)
	assert opponent.hit_points == max(0, opponent_init_hp - expected_damage)


def test_combatant_attack_fatal(mocker):
	"""
	Test case for Combatant attack that kills the opponent
	"""
	combatant = combatant_setup()
	opponent = opponent_setup()
	# Make opponent feeble enough to die in 1 hit
	opponent.hit_points = 1
	mocker.patch('src.models.Dice.roll', return_value=20)
	combatant.attack(opponent)
	assert not opponent.is_alive


@pytest.mark.parametrize(
	'dice_roll, strength, expected_damage, survive',
	[
		(9, 12, 2, True),  # Attack should hit since modifier +1
		(9, 10, 0, True),  # Attack should miss since modifier +0
		(5, 20, 6, False),  # Attack should hit since modifier +5
		(10, 9, 0, True),  # Attack should miss since modifier -1
		(14, 1, 0, True),  # Attack should miss since modifier -5
		(15, 1, 1, True),  # Attack should still hit with roll 15+
		(20, 10, 2, True),  # Attack should crit and damage doubled
		(20, 9, 1, True),  # Attack should crit and modifer -1 to damage
		(20, 1, 1, True),  # Attack should crit and modifer -5 to damage
		(20, 20, 12, False),  # Attack should crit and double modifer to damage
	]
)
def test_combatant_attack_with_modifier(mocker, dice_roll, strength, expected_damage, survive):
	"""
	Test case for Combatant attack with various modifier scenarios
	"""
	combatant = combatant_setup()
	combatant.strength = strength
	opponent = opponent_setup()
	mocker.patch('src.models.Dice.roll', return_value=dice_roll)
	opponent_init_hp = opponent.hit_points
	combatant.attack(opponent)
	assert opponent.hit_points == max(0, opponent_init_hp - expected_damage)
	assert opponent.is_alive == survive
