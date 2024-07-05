from src.models import Character


def test_character_name():
    name_to_assign = 'Nathan'
    nathan_character = Character(name=name_to_assign)
    assert nathan_character.get_name() == name_to_assign
