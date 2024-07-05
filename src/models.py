from enum import Enum


class Character:
    name: str
    alignment: Alignment

    def __init__(self, **kwargs):
        self.set_name(kwargs.get('name', ''))
        self.set_alignment(kwargs.get('alignment', Alignment.NEUTRAL))

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_alignment(self, alignment: Alignment):
    	self.alignment = alignment

    def get_alignment(self):
    	return self.alignment


class Alignment(Enum):
	GOOD = 'good'
	EVIL = 'evil'
	NEUTRAL = 'neutral'
