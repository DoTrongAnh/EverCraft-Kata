from src.models import (
	Alignment, Character
)


CHARACTER_NAME = 'Nathan'
CHARACTER_ALIGNMENT = Alignment.GOOD


def character_setup() -> Character:
	"""
	Set up a character for test cases related to Character functionalities
	"""
	character = Character(
		name=CHARACTER_NAME,
		alignment=CHARACTER_ALIGNMENT
	)
	return character


def test_character_name():
	"""
	Test case for Character name getter and setter
	"""
	character = character_setup()
	assert character.name == CHARACTER_NAME


def test_character_alignment():
	"""
	Test case for Character alignment getter and setter
	"""
	character = character_setup()
	assert character.alignment == CHARACTER_ALIGNMENT
