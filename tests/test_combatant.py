from src.models import (
	Alignment, Combatant
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


def test_combatant_attack_missed(mocker):
	"""
	Test case for Combatant attack when missed (roll too low)
	"""
	combatant = combatant_setup()
	opponent = opponent_setup()
	# Since default armor_class is 10, mock roll to be lower
	mocker.patch('src.models.Dice.roll', return_value=9)
	opponent_init_hp = opponent.hit_points
	combatant.attack(opponent)
	assert opponent.hit_points == opponent_init_hp


def test_combatant_attack_hit(mocker):
	"""
	Test case for Combatant attack when hit (roll high enough)
	"""
	combatant = combatant_setup()
	opponent = opponent_setup()
	# Since default armor_class is 10, mock roll to be at least 10
	mocker.patch('src.models.Dice.roll', return_value=10)
	opponent_init_hp = opponent.hit_points
	combatant.attack(opponent)
	assert opponent.hit_points == opponent_init_hp - 1


def test_combatant_attack_crit(mocker):
	"""
	Test case for Combatant attack when critical hit (roll 20)
	"""
	combatant = combatant_setup()
	opponent = opponent_setup()
	mocker.patch('src.models.Dice.roll', return_value=20)
	opponent_init_hp = opponent.hit_points
	combatant.attack(opponent)
	assert opponent.hit_points == opponent_init_hp - 2


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
